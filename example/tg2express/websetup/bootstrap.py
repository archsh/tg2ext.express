# -*- coding: utf-8 -*-
"""Setup the tg2express application"""
from __future__ import print_function

import logging
from tg import config
from tg2express import model
import transaction


def bootstrap(command, conf, vars):
    """Place any commands to setup tg2express here"""

    # <websetup.bootstrap.before.auth
    from sqlalchemy.exc import IntegrityError

    try:
        u = model.User()
        u.user_name = 'manager'
        u.display_name = 'Example manager'
        u.email_address = 'manager@somedomain.com'
        u.password = 'managepass'

        model.DBSession.add(u)

        g = model.Group()
        g.group_name = 'managers'
        g.display_name = 'Managers Group'

        g.users.append(u)

        model.DBSession.add(g)

        p = model.Permission()
        p.permission_name = 'manage'
        p.description = 'This permission give an administrative right to the bearer'
        p.groups.append(g)

        model.DBSession.add(p)

        u1 = model.User()
        u1.user_name = 'editor'
        u1.display_name = 'Example editor'
        u1.email_address = 'editor@somedomain.com'
        u1.password = 'editpass'

        model.DBSession.add(u1)
        model.DBSession.flush()
        transaction.commit()
    except IntegrityError:
        print('Warning, there was a problem adding your auth data, it may have already been added:')
        import traceback

        print(traceback.format_exc())
        transaction.abort()
        print('Continuing with bootstrapping...')

        # <websetup.bootstrap.after.auth>

    try:
        w1 = model.Writer(firstname='Mingcai', lastname='SHEN')
        w2 = model.Writer(firstname='Fangze', lastname='SHEN')
        a1 = model.Article(title='Test note1', keys='test,note,another', content=u'This is just a test note1')
        a2 = model.Article(title='Test note2', keys='note,another', content=u'This is just a test note2')
        a3 = model.Article(title='Test note3', keys='test,another', content=u'This is just a test note3')
        a4 = model.Article(title='Test note4', keys='test', content=u'This is just a test note4')
        c1 = model.Comment(comment='Good! Thanks.')
        c2 = model.Comment(comment='Well, ok!')
        a4.comments.append(c1)
        a4.comments.append(c2)
        w1.articles.append(a1)
        w1.articles.append(a3)
        w2.articles.append(a2)
        w2.articles.append(a4)
        model.DBSession.add_all([w1, w2])
        model.DBSession.flush()
        transaction.commit()
    except IntegrityError:
        print('Warning, there was a problem adding your auth data, it may have already been added:')
        import traceback

        print(traceback.format_exc())
        transaction.abort()
        print('Continuing with bootstrapping...')