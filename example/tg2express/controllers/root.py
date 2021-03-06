# -*- coding: utf-8 -*-
"""Main Controller"""

from tg import expose, flash, require, lurl, request, redirect, tmpl_context
from tg.i18n import ugettext as _, lazy_ugettext as l_
from tg import predicates, config
from tgext.admin.tgadminconfig import TGAdminConfig
from tgext.admin.controller import AdminController
import logging
from tg2express import model
from tg2express.controllers.secure import SecureController
from tg2express.model import DBSession
from tg2express.lib.base import BaseController
from tg2express.controllers.error import ErrorController
from tg2ext.express.controller import ExpressController
logger = logging.getLogger('tg2express')

__all__ = ['RootController']


class ArticleController(BaseController):

    @expose()
    def _lookup(self, *reminders):
        from tg2express.model.articles import Article
        return ExpressController(model=Article, dbsession=DBSession)


class RootController(BaseController):
    """
    The root controller for the tg2express application.

    All the other controllers and WSGI applications should be mounted on this
    controller. For example::

        panel = ControlPanelController()
        another_app = AnotherWSGIApplication()

    Keep in mind that WSGI applications shouldn't be mounted directly: They
    must be wrapped around with :class:`tg.controllers.WSGIAppController`.

    """
    secc = SecureController()
    admin = AdminController(model, DBSession, config_type=TGAdminConfig)
    error = ErrorController()

    writer = ExpressController(model=model.Writer, dbsession=DBSession,
                               allow_only=None)  # predicates.has_permission('administration'))
    article = ExpressController(model=model.Article, dbsession=DBSession,
                                allow_only=None)  # predicates.not_anonymous())
    comment = ExpressController(model=model.Comment, dbsession=DBSession,
                                allow_only=None)

    def _before(self, *args, **kw):
        #logger.info("config: %s", config['tg.app_globals'].sa_engine)
        logger.info("args: %s", args)
        logger.info("kw: %s", kw)
        tmpl_context.project_name = "tg2express"

    @expose('tg2express.templates.index')
    def index(self):
        """Handle the front-page."""
        return dict(page='index')

    @expose('tg2express.templates.about')
    def about(self):
        """Handle the 'about' page."""
        return dict(page='about')

    @expose('tg2express.templates.environ')
    def environ(self):
        """This method showcases TG's access to the wsgi environment."""
        return dict(page='environ', environment=request.environ)

    @expose('tg2express.templates.data')
    @expose('json')
    def data(self, **kw):
        """This method showcases how you can use the same controller for a data page and a display page"""
        return dict(page='data', params=kw)

    @expose('tg2express.templates.index')
    @require(predicates.has_permission('manage', msg=l_('Only for managers')))
    def manage_permission_only(self, **kw):
        """Illustrate how a page for managers only works."""
        return dict(page='managers stuff')

    @expose('tg2express.templates.index')
    @require(predicates.is_user('editor', msg=l_('Only for the editor')))
    def editor_user_only(self, **kw):
        """Illustrate how a page exclusive for the editor works."""
        return dict(page='editor stuff')

    @expose('tg2express.templates.login')
    def login(self, came_from=lurl('/')):
        """Start the user login."""
        login_counter = request.environ.get('repoze.who.logins', 0)
        if login_counter > 0:
            flash(_('Wrong credentials'), 'warning')
        return dict(page='login', login_counter=str(login_counter),
                    came_from=came_from)

    @expose()
    def post_login(self, came_from=lurl('/')):
        """
        Redirect the user to the initially requested page on successful
        authentication or redirect her back to the login page if login failed.

        """
        if not request.identity:
            login_counter = request.environ.get('repoze.who.logins', 0) + 1
            redirect('/login',
                     params=dict(came_from=came_from, __logins=login_counter))
        userid = request.identity['repoze.who.userid']
        flash(_('Welcome back, %s!') % userid)
        redirect(came_from)

    @expose()
    def post_logout(self, came_from=lurl('/')):
        """
        Redirect the user to the initially requested page on logout and say
        goodbye as well.

        """
        flash(_('We hope to see you soon!'))
        redirect(came_from)
