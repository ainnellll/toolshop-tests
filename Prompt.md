# Prompts and AI tool

**AI tool and model used:** Chatgpt, model: GPT-5.6,

## Prompt 1(screenshots)
Тест загрузился и запустился: в терминале 2failed. почему ошибка вышла? дай инструктор как можно исправить

## Prompt 2(screenshots)
5 тестов , упал 2 (2 failed, 5 passed). Упали тест входа с правильным паролем (valid_credentials) и тест покупки. Оба работали ещё недавно. в чем может быт проблема

# SIS 3 — CI pipeline (AI usage)

**AI tool and model used:** Claude (Anthropic), model: Claude Sonnet 5.5.

## Example 1: all CI jobs were red

**Prompt:** I sent the screenshot of the failed GitHub Actions log (step "Run Playwright tests") and asked why all four shards fail, although the tests pass on my computer (7 passed).

**What the AI said:** the page snapshot in the log showed Cloudflare's "Performing security verification" page, i.e. the public site blocks GitHub-hosted runners, so the tests never see the shop. It suggested running the Toolshop app in Docker inside the workflow and pointing the tests to `http://localhost:4200`.

**What I did and checked:** I read the log myself, confirmed the Cloudflare page in the snapshot, added the Docker step to `playwright.yml`, and pushed. The run was still red, which led to the second problem.

## Example 2: the products API returned HTTP 500

**Prompt:** I sent the log of the Docker step with the API check (`GET /products -> 500`) and the `ls -la storage` output.

**What the AI said:** the web server user could not write to the Laravel `storage` folder (wrong owner and permissions), so every request that needs cache or logs failed. It suggested a `chmod -R 777 storage bootstrap/cache` step after `composer install`.

**What I did and checked:** I added the line to the workflow, pushed, and checked in the next run that `/brands` and `/products` return 200 and all 4 shards are green. I also measured the runtime myself: 4 min 30 s with 1 job and 5 min 22 s with 4 shards, and wrote the honest conclusion in the README.
