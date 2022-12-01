from tardis_dev import datasets

print(datasets.download(
    exchange="deribit",
    data_types=[
        "incremental_book_L2",
        "trades",
        "quotes",
        "derivative_ticker",
        "book_snapshot_25",
        "liquidations"
    ],
    from_date="2019-11-01",
    to_date="2019-11-02",
    symbols=["ETH-OPTIONS"],
    api_key="YOUR API KEY (optionally)",
)
)

