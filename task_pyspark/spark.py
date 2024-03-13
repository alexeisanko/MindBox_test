from pyspark.sql import SparkSession


def load_simple_data(spark):
    categories_df = spark.createDataFrame(
        [(x, f"Category_{x}") for x in range(1, 7)],
        ["id", "name"]
    )

    products_df = spark.createDataFrame(
        [(x, f"Product_{x}") for x in range(1, 11)],
        ["id", "name"]
    )

    product_off_category = spark.createDataFrame([
        (1, 1),
        (1, 2),
        (2, 2),
        (3, 4),
        (3, 2),
        (4, 5),
        (6, 5),
        (7, 8),
        (6, 8),
        (7, 2),
        (1, 8),
        (6, 9),
        (3, 10)],
        ["category_id", "product_id", ]
    )

    return categories_df, products_df, product_off_category


def join_data(categories_df, products_df, product_off_category):
    data_df = (
        products_df.join(
            product_off_category,
            products_df.id == product_off_category.product_id, how='left'
        ).join(
            categories_df,
            product_off_category.category_id == categories_df.id, how='left'
        ).select(['category_name', 'product_name'])
    )
    return data_df


if __name__ == '__main__':
    spark = SparkSession.builder \
        .appName("dataframes") \
        .getOrCreate()

    categories_df, products_df, product_off_category = load_simple_data(spark)
    data_df = join_data(categories_df, products_df, product_off_category)
    data_df.orderBy("category_id", "product_id", ).show(truncate=True)

    spark.stop()
