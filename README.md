# toolshop-tests

[![Playwright Tests](https://github.com/ainnellll/toolshop-tests/actions/workflows/playwright.yml/badge.svg?branch=main)](https://github.com/ainnellll/toolshop-tests/actions/workflows/playwright.yml)

Autotests for https://practicesoftwaretesting.com (Python, pytest, Playwright, Page Object).

## Running locally

```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
playwright install
pytest
```

## CI

**CI system:** GitHub Actions. It is built into GitHub, where the repository already lives, needs no server of its own, is free for public repositories and supports a matrix for splitting tests across parallel jobs.

**Pipeline** (`.github/workflows/playwright.yml`):
- runs on every push and every pull request (also manually via `workflow_dispatch`);
- `actions/setup-python` with `cache: pip`, then `pip install -r requirements.txt`;
- `playwright install --with-deps chromium`, then the full suite (no `-k` / `-m` filters);
- the Toolshop app is started in Docker on the runner and the tests run against `http://localhost:4200`, because the public site is protected by Cloudflare, which blocks GitHub-hosted runners;
- the suite is split into 4 shards running in parallel (`pytest-split`: `--splits 4 --group N`);
- the `merge-reports` job merges the JUnit files of all shards into one `junit-merged.xml`;
- artefacts (kept 14 days): `playwright-report-N` (HTML report + JUnit), `test-results-N` (traces, screenshots, videos), `junit-report` (merged).

**CI settings** (`pytest-ci.ini`, used as `pytest -c pytest-ci.ini`):

| Playwright Test (JS) feature | What is used here (Python) |
| --- | --- |
| `retries: 2` | `pytest-rerunfailures`: `--reruns 2` |
| JUnit reporter | built-in `--junitxml=reports/junit.xml` |
| HTML report | `pytest-html`: `--html=reports/report.html` |
| `trace: 'on-first-retry'` | `--tracing retain-on-failure` (plus screenshot and video on failure) |
| `forbidOnly: true` | a hook in `conftest.py`: when `CI` is set, any test marked `@pytest.mark.only` fails the run |
| `--shard=i/n` | `pytest-split`: `--splits n --group i` |

`forbidOnly`, `--shard` and the `blob` reporter belong to the JavaScript Playwright Test runner; the Python plugin does not have them, so the equivalents above are used.

### Runtime

| Configuration | Total run time | Run tests step (slowest shard) | Run |
| --- | --- | --- | --- |
| 1 job, no sharding | 4 min 30 s | 19 s | [run](https://github.com/ainnellll/toolshop-tests/actions/runs/44887406749) |
| 4 shards + merge | 5 min 22 s | 11 s | [run](https://github.com/ainnellll/toolshop-tests/actions/runs/44883502881) |

Single run for each configuration. Conclusion: sharding made the tests themselves faster (19 s to 11 s in the slowest shard), but the total time did not drop, because every shard has to start its own copy of the Toolshop app in Docker (about 4 minutes) and the suite has only 7 tests, so the fixed setup time dominates.

### Running the CI configuration locally

```
pip install -r requirements.txt
playwright install --with-deps chromium
$env:CI="true"; pytest -c pytest-ci.ini
```

## AI usage

See [Prompt.md](./Prompt.md).