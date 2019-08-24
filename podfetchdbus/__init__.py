# -*- coding: utf-8 -*-

from .__version__ import __version__
__author__ = 'Alexander Keil'
__email__ = 'akeil@akeil.de'

from .plugin import start
from .plugin import stop

from .plugin import on_updates_complete
from .plugin import on_subscription_updated
from .plugin import on_subscription_added
from .plugin import on_subscription_removed
