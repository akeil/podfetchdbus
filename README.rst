##############
Podfetch D-Bus
##############
D-Bus plugin for Podfetch.

This plugin is intended for the Podfetch "daemon-mode"
and makes Podfetch available trough D-Bus.
The Podfetch interface is made available under the user's session bus.

:Path: ``/de/akeil/Podfetch``
:Interface: ``de.akeil.Podfetch``

The D-Bus interface can be used to interact with a running Podfetch instance
from within other applications, such as desktop applets.


Installation
############
Install with pip.
The ``podfetch`` app should find this plugin automatically.


D-Bus Interface
###############


Methods
=======

:Update():
    Trigger an update on all subscriptions.
:UpdateOne(String name):
    Update the given episode.
:Episodes(Int32 limit):
    List the ``limit`` most recent episodes.
:AddSubscription(String url, String name):
    Subscribe to a podcast.
:RemoveSubscription(String name, Boolean delete):
    Unsubscribe, optionally delete downloaded files.
:ShowSubscription(String name):
    Show details for a single subscription.
:DisableSubscription(String name):
    Disable a subscription (will not be updated).
:EnableSubscription(String name):
    Enable a subscription

Generally, all methods that work on a subscription expect the subscription
name as a parameter and will raise ``NotFoundException``
if there is no subscription with that name.

The *Episodes* method returns a list of structs with the following properties::

    (
        Episode ID
        Subscription Name (for that episode)
        Episode Title
        Pub Date (year, month, day, hour, minute, second)
        Files (url, content-type, local file)
    )


Signals
=======
Clients can subscribe to the following signals:

:SubscriptionAdded:     After a subscription was successfully added.
:SubscriptionRemoved:   When a subscription was deleted.
:SubscriptionUpdated:   After a *single* subscription was updated.
:UpdatesComplete:       When an update run (for all subscriptions) is complete.
