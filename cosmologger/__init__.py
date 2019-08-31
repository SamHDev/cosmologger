import sys
import datetime

# Logger Config Handler
import sys

try:
    default_app_name = sys.modules['__main__'].__file__.rsplit("/", 1)[1].split(".", 1)[0]
except:
    default_app_name = "main"

default_colour = True
default_debug = False

logger_colours = dict(reset="\u001b[0m", white="\u001b[37m", black="\u001b[30m", red="\u001b[31m", green="\u001b[32m",
                      yellow="\u001b[33m", blue="\u001b[34m", purple="\u001b[35m", cyan="\u001b[36m")

logger_style = {
    "root": "{app}> {colour_pre} {time} [{type}] {msg}{colour_suf}",
    "info": "INFO",
    "ok": "-OK-",
    "warn": "WARN",
    "error": "ERRR",
    "fatal": "FATL",
    "debug": "DBUG",
    "separator": "-" * 70
}


def _log(text: str):
    sys.stdout.write(text + "\n")
    sys.stdout.flush()


class Logger:
    """
    Logging Class

    :param debug: Output Debug Logging Message
    :type debug: bool
    :param app_name: The AppName to Log With.
    :type app_name: str
    :param style: Style Formatting (Format Dict)
    :type style: dict
    :param colour: Output Colours in Logging Message
    :type colour: bool

    """
    def __init__(self, debug: bool = None, app_name: str = None, style: dict = None, colour: bool = None):
        self.print_debug = debug
        self.app_name = app_name
        self.style = style
        self.colour = colour
        if style is None:
            self.style = logger_style
        if app_name is None:
            self.app_name = default_app_name
        if colour is None:
            self.colour = default_colour
        if debug is None:
            self.print_debug = default_debug

    def _format(self, log_type: str, log_msg: str, app_name: str = None, colour: str = None):
        """
        Formats a String to Log.

        :param log_type: The logging Type String. Either Format Key or Raw String
        :type log_type: str
        :param log_msg: The Message to Be Logged
        :type log_msg: str
        :param app_name: The Logging App Name String. If not Specified uses default
        :type app_name: str
        :param colour: The Color String to Be used. If not Specified no color is used
        :type colour: str

        :returns: Formatted String In Style of Logger
        :rtype: str
        """

        if app_name is None:
            app_name = self.app_name
        if log_type in self.style.keys():
            log_type = self.style[log_type]

        f_time = datetime.datetime.utcnow().strftime("%H:%M:%S")
        colour_pre = ""
        colour_suf = ""
        if not self.colour:
            colour = None
        if colour is not None:
            if colour in logger_colours.keys():
                colour_pre = logger_colours[colour]
            else:
                colour_pre = colour
            colour_suf = logger_colours["reset"]
        return self.style["root"].format(app=app_name, time=f_time, type=log_type,
                                         msg=log_msg, colour_pre=colour_pre,
                                         colour_suf=colour_suf)

    def log(self, log_type: str, log_msg: str, app_name: str = None, colour: str = None):
        """
        Formats a String to Log.

        :param log_type: The logging Type String. Either Format Key or Raw String
        :type log_type: str
        :param log_msg: The Message to Be Logged
        :type log_msg: str
        :param app_name: The Logging App Name String. If not Specified uses default
        :type app_name: str
        :param colour: The Color String to Be used. If not Specified no color is used
        :type colour: str

        :returns: The message output to logger.
        :rtype: str
        """
        to_log = self._format(log_type, log_msg, app_name=app_name, colour=colour)
        _log(to_log)
        return to_log

    def __call__(self, msg: str):
        """
        Log as debug

        :param msg: The message to log
        :type msg: str
        """
        self.debug(msg)

    def info(self, msg: str):
        """
        Log as info

        :param msg: The message to log
        :type msg: str
        """
        self.log("info", msg, colour="cyan")

    def ok(self, msg: str):
        """
        Log as ok

        :param msg: The message to log
        :type msg: str
        """
        self.log("ok", msg, colour="green")

    def warn(self, msg: str):
        """
        Log as warning

        :param msg: The message to log
        :type msg: str
        """
        self.log("warn", msg, colour="yellow")

    def warning(self, msg: str):
        """
        Log as warning

        :param msg: The message to log
        :type msg: str
        """
        self.warn(msg)

    def error(self, msg: str):
        """
        Log as error

        :param msg: The message to log
        :type msg: str
        """
        self.log("error", msg, colour="red")

    def fatal(self, msg: str):
        """
        Log as fatal

        :param msg: The message to log
        :type msg: str
        """
        self.log("fatal", msg, colour="purple")

    def critical(self, msg: str):
        """
        Log as fatal

        :param msg: The message to log
        :type msg: str
        """
        self.fatal(msg)

    def debug(self, msg: str):
        """
        Log as debug

        :param msg: The message to log
        :type msg: str
        """
        if self.print_debug:
            self.log("debug", msg)

    def sep(self):
        """
        Log a Separator
        """
        self.separator()

    def separator(self):
        """
        Log a Separator
        """
        _log(self.style["separator"])


class SubLogger(Logger):
    def __init__(self, app_name, debug=None, style=None, color=None, parent=None):
        if parent is not None:
            debug = parent.print_debug
            style = parent.style
            color = parent.color
            self.parent = parent
        super().__init__(debug=debug, app_name=app_name, style=style, color=color)
