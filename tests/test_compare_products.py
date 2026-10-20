from playwright.sync_api import expect


def test_comparison_shows_the_two_chosen_products(product_page, comparison_page):
    product_page.open_home()
    expect(product_page.cards.nth(1)).to_be_visible()

    # запоминаем название и цену двух первых товаров каталога
    first = (product_page.card_name(0), product_page.card_price(0))
    second = (product_page.card_name(1), product_page.card_price(1))

    product_page.add_to_compare(0)
    product_page.add_to_compare(1)
    product_page.open_comparison()

    # в таблице ровно два товара
    expect(comparison_page.names).to_have_count(2)

    # названия те же, что в каталоге (порядок столбцов не важен)
    shown_names = sorted(t.strip() for t in comparison_page.names.all_inner_texts())
    assert shown_names == sorted([first[0], second[0]])

    # цены те же, что в каталоге
    expect(comparison_page.price_cell(first[1])).to_be_visible()
    expect(comparison_page.price_cell(second[1])).to_be_visible()