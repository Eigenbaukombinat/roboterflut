class BotRegistry(object):
    _bots = {}

    def add_bot(self, name, ctrl):
        self._bots[name] = dict(ctrl=ctrl)

    def get_driver(self, name):
        """returns bot driver for given name, or None if no bot is found."""
        bot = self._bots.get(name)
        if bot is not None:
            return bot['ctrl']
