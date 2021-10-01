# /usr/bin/env python3
# Decorator Classes.


class logit(object):

    _logfile = "out.log"

    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        log_string = self.func.__name__ + " was called."
        with open(self._logfile, "a") as opened_file:
            # Now we log to the specified logfile.
            opened_file.write(log_string + "\n")
        # Now, send a notification.
        self.notify()

        # Return base function.
        return self.func(*args)

    def notify(self):
        # Logit only logs, no more.
        pass


logit._logfile = "out.log"  # if change logfile.


@logit
def myfunc1():
    pass


myfunc1()


class email_logit(logit):
    """
    A logit implementation for sending emails to admins
    when the function is called.
    """

    def __init_(self, email="admin@myproject.com", *args, **kwargs):
        self.email = email
        super(email_logit, self).__init__(*args, **kwargs)

    def notify(self):
        # Send an email to self.email.
        # Will not be implemented here.
        pass
