# Cosmo Logger
A Simple yet Nicely formatted Logger for all your Logging Needs. Made for the Cosmo Project

## Key Features

 * Simple to Use. 
 * Supports Colors
 * Configurable Styles



## Installation
You can install via python's `pip` module:

Install with Offical Python Package Index:
```bash
python3 -m pip install cosmologger
```
or with this Git Respiratory
```bash
python3 -m pip install git+https://github.com/SamHDev/cosmologger.git
```
*Note for Noobies: If `python3` work then use `python`*



## Usage

##### Importing the Library

You can import the library with the following statement:
```python
import cosmologger
```

##### Creating a Logging Object

To Start logging, create a logger object. 
This can be placed in the module or in a class so it can be accessed around the project.
```python
logger = cosmologger.Logger()
```

The Logger Object can be created with options such `debug` and `app_name` as shown below: 
```python
logger = cosmologger.Logger(
    debug = True,             # Enables Debug Print
    app_name = "CORE APP",    # Set App Name to Print
    style = None,             # Set Style Formating (Format Dict)
    color = None              # Enable Color Print
)
```

##### Logging Example

To output messages to the logger/console you can call the many functions found in the Logger Class.

Here is a simple Example of each Method.

```python
logger.info("This a 'Info' Message")
logger.ok("This a 'Ok' Message")
logger.warn("This a 'Warn' Message")
logger.error("This a 'Error' Message")
logger.fatal("This a 'Fatal' Message")
logger.debug("This a 'Debug' Message")
logger("This a 'Debug' Message but Simpler")
logger.log("TEST", "This is a Custom Logging Output Type")
```
The above code would produce the resulting output:
```
main>  10:03:18 [INFO] This a 'Info' Message
main>  10:03:18 [-OK-] This a 'Ok' Message
main>  10:03:18 [WARN] This a 'Warn' Message
main>  10:03:18 [ERRR] This a 'Error' Message
main>  10:03:18 [FATAL] This a 'Fatal' Message
main>  10:03:18 [Debug] This a 'Debug' Message
main>  10:03:18 [Debug] This a 'Debug' Message but Simpler
main>  10:03:18 [TEST] This is a Custom Logging Output Type
```

##### Logging Methods

| Type | Output | Methods |
| --- | --- | --- |
| Info | `[INFO]` | `Logger.info(msg)` |
| Ok | `[-OK-]` | `Logger.ok(msg)` |
| Warning | `[WARN]` | `Logger.warn(msg)` `Logger.warning(msg)` |
| Error | `[ERROR]` | `Logger.error(msg)` |
| Fatal | `[FATL]` | `Logger.fatal(msg)` `Logger.critical(msg)` |
| Debug | `[DBUG]` | `Logger.debug(msg)` `Logger(msg)` |

###### Custom Logging

Custom Logging Types is a simple as so:

```python
logging.log("Custom Type", "Message")
```

##### Sub Loggers (For Multiple Classes/Modules)

A SubLogger can be used for classes/modules across large projects. 
The `cosmoLogger.SubLogger` is a subclass of `cosmoLogger.Logger` and contains all the methods
However, the class requires the `app_name` parameter and has the optinal `parent` paramater that
copies the settings from the 'parent' Logger Object.

It can be used like so:
```python
sublogger = logger.SubLogger("SUB APP", parent=logger)
```

## License and Attributes

Created by Sam Huddart under alias [SamHDev](https://github.com/SamHDev/) for the [Blume Open Source Project](https://www.youtube.com/watch?v=oHg5SJYRHA0). `SamHDev/cosmologger` is licensed under the GNU General Public License v3.0 and is Open-Source as seen in [LICENSE](LICENSE). Commercial use, Modification and Distribution are permmited. Although credit is not necessary, it is much obliged. If you do wish to credit the author, please link the [respiratory](https://github.com/SamHDev/tcpnonblock/) and the author at [github](https://github.com/SamHDev/) or [website](https://samhdev.com). Thank you for using our work.
