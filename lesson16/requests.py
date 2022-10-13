from psycopg2 import connect


def get_all_ads(cursor: connect, is_published: bool = True) -> list:
    """
    Search for all current ads.
    """

    is_published = 'TRUE' if is_published else 'FALSE'

    cursor.execute(
        f"""
        SELECT  ads.name,
                ads.price,
                ads.description,
                author.author,
                address.address
        FROM ads
        JOIN author ON ads.fk_author = author.pk_id
        JOIN address ON ads.fk_address = address.pk_id
        WHERE is_published = {is_published}
        """
    )

    return cursor.fetchall()


def get_ads_by_author(cursor: connect, author: str) -> list:
    """
    Search for current ads according to the specified author.
    """

    cursor.execute(
        f"""
        SELECT  ads.name,
                ads.price,
                ads.description,
                author.author,
                address.address
        FROM ads
        JOIN author ON ads.fk_author = author.pk_id
        JOIN address ON ads.fk_address = address.pk_id
        WHERE author.author = '{author}'
        """
    )

    return cursor.fetchall()


def get_ads_by_author_and_price(cursor: connect, author: str, price: str) -> list:
    """
    Search for current ads according to the specified author and price.
    """

    cursor.execute(
        f"""
        SELECT  ads.name,
                ads.price,
                ads.description,
                author.author,
                address.address
        FROM ads
        JOIN author ON ads.fk_author = author.pk_id
        JOIN address ON ads.fk_address = address.pk_id
        WHERE author.author = '{author}' AND ads.price = {price}
        """
    )

    return cursor.fetchall()


def get_ads_by_city(cursor: connect, city: str) -> list:
    """
    Search for current ads in accordance with the specified city.
    """

    cursor.execute(
        f"""
        SELECT  ads.name,
                ads.price,
                ads.description,
                author.author,
                address.address
        FROM ads
        JOIN author ON ads.fk_author = author.pk_id
        JOIN address ON ads.fk_address = address.pk_id
        WHERE address.address LIKE '{city}%'
        """
    )

    return cursor.fetchall()


def get_ads_by_price_range(cursor: connect, starting_price: str, final_price: str) -> list:
    """
    Search for current ads in accordance with the specified price range.
    """

    cursor.execute(
        f"""
        SELECT  ads.name,
                ads.price,
                ads.description,
                author.author,
                address.address
        FROM ads
        JOIN author ON ads.fk_author = author.pk_id
        JOIN address ON ads.fk_address = address.pk_id
        WHERE ads.price >= {starting_price} AND ads.price <= {final_price}
        ORDER BY ads.price
        """
    )

    return cursor.fetchall()
