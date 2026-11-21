python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
playwright install
pytest
### Runtime

| Configuration | Total run time | Run tests step (slowest shard) | Run |
| --- | --- | --- | --- |
| 1 job, no sharding | X min Y s | X s | [run](ССЫЛКА_ДО) |
| 4 shards + merge | 5 min 22 s | 11 s | [run](https://github.com/ainnellll/toolshop-tests/actions/runs/44883502881) |