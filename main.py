from scraper import headless_fetch
from bs4 import BeautifulSoup
import os


def asda(item):
    # Classes for HTML Parser
    item_sel = ".co-product"
    p_price_sel = ".co-product__price"
    u_price_sel = ".co-item__price-per-uom-msg"
    title_sel = ".co-product__anchor"

    print("Fetching result from ASDA..")

    # Grab page and parse
    page = headless_fetch(
        f"https://groceries.asda.com/search/{item}", ".co-item")
    soup = BeautifulSoup(page, "html.parser")
    item_el = soup.select_one(item_sel)
    price_p_el = item_el.select_one(p_price_sel)
    price_p_fr = " ".join(price_p_el.text.split(" ")[2:])
    price_u_el = item_el.select_one(u_price_sel)
    title = item_el.select_one(title_sel).text

    result = f"{price_p_fr} {price_u_el.text} ({title})"

    return result


def morrisons(item):
    # Classes for HTML Parser
    item_sel = ".product-card-container"
    p_price_sel = ".price-pack-size-container"
    u_price_sel = "span[data-test='fop-price-per-unit']"
    title_sel = "h3[data-test='fop-title']"

    print("Fetching result from Morrisons..")

    # Grab page and parse
    page = headless_fetch(
        f"https://groceries.morrisons.com/search?q={item}", item_sel)
    soup = BeautifulSoup(page, "html.parser")
    item_el = soup.select_one(item_sel)
    price_p = item_el.select_one(
        p_price_sel).findAll("span")[1].text
    price_u = item_el.select_one(u_price_sel).text
    title = item_el.select_one(title_sel).text

    result = f"{price_p} {price_u} ({title})"

    return result


os.system("clear")
print("-- Shop Price Comparison Tracker --")
query = input("Product search term: ")
res_asda = asda(query)
res_morrisons = morrisons(query)

print(f"ASDA: {res_asda}")
print(f"Morrisons: {res_morrisons}")
