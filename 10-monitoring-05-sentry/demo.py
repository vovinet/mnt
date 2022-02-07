import sentry_sdk
sentry_sdk.init(
    "https://a538774bccac4e97ac10acbb6bab3361@o1137342.ingest.sentry.io/6189853",

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
)

division_by_zero = 1 / 0
