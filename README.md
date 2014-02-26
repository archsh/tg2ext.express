tg2ext.express
==============

A small extension for TurboGears2

For example:

    from tg2ext.express import ExpressController

    class ExampleModel(DeclarativeBase):
        __tablename__ = 'examples'

        #{ Columns
        id = Column(Integer, primary_key=True)
        data = Column(Unicode(256), nullable=False)
        created = Column(DateTime, default=func.NOW())
        #}

    class RootController(BaseController):
        # ...
        examples = ExpressController(model=ExampleModel, dbsession=DBSession)

        # ...

