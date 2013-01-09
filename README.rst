
Events API: Raw Events
----------------------

This profile lets you access raw events from the Bitdeli :ref:`events-api`.

Contact `support@bitdeli.com <mailto:support@bitdeli.com>`_ if you would like
to utilize custom events and :ref:`events-api` in a way that is not supported by
this profile.

- **Source:** Events from your application, sent to the :ref:`events-api`

- **Historical data:** All historical data.

- **Retention:**
    - *Premium*: 2000 latest events per user and 365 days of inactive users.
    - *Advanced*: 500 latest events per user and 90 days of inactive users.
    - *Basic*: 100 latest events per user and 30 days of inactive users.

  Inactive users who have not produced any events for the last *N* days, where *N*
  depends on the plan as defined above, are purged from profiles.

- **Schema:**
    .. code-block:: python

         {
             "events": [
                [
                    timestamp,
                    group_key,
                    ip_address,
                    event
                ],
                ...
            ]
         }

    where *timestamp* is a server-side timestamp in UTC, *group_key* identifies the batch
    in which the event was processed, *ip_address* is the IP address of the sender,
    and *event* is the event object sent to :ref:`events-api`.

- **Update interval:** 1 hour

- **Code:** `bitdeli/profile-events-raw <https://github.com/bitdeli/profile-events-raw>`_
