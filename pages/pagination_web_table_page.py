from .base_page import BasePage

class PaginationWebTablePage(BasePage):
    table_selector = '#productTable'
    pagination_selector = '#pagination li a'
    def __init__(self, page):
        super().__init__(page)


    def get_all_products_and_total_price(self):
        all_products = []
        total_price = 0
        page = self.page

        page.wait_for_selector(self.pagination_selector)
        pages = page.query_selector_all(self.pagination_selector)
        num_pages = len(pages)
        for i in range(1, num_pages + 1):
            page.click(f'#pagination li:nth-child({i}) a')
            page.wait_for_selector(self.table_selector)

            rows = page.query_selector_all(f'{self.table_selector} tbody tr')
            for row in rows:
                cells = row.query_selector_all('td')
                id_ = cells[0].inner_text()
                name = cells[1].inner_text()
                price_text = cells[2].inner_text()
                price = float(price_text.replace('$', ''))
                all_products.append({'id': id_, 'name': name, 'price': price})
                total_price += price
        return {'all_products': all_products, 'total_price': total_price} 