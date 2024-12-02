def before_all(context):
    context.config.setup_logging()

def after_all(context):
    context.config.teardown_logging()