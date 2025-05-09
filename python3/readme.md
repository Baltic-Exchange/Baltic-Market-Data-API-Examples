# Python example

This example demonstrates making calls to the Baltic Exchange Market Data API using Python.

It assumes you've made a feed and got an API Key. You can do this here: https://api.balticexchange.com.

Steps:

* Go to the Market Data API Portal: https://api.balticexchange.com and login
* Create a feed (the code example assumes you'll make a v1.3 JSON feed)
* Get your **API Key** and **Feed ID** (see the documentation for where you can find these)
* Ensure Python 3 is installed
* Run the **main.py** file

The script will prompt you for you **API Key** and **Feed ID**. Once entered, you'll see the JSON output from the two calls:

* Last datum change on (latestDatumChangeOn)
* Get data (data)

You can also run the script with arguments like this:

    main.py --feedid [your feed id] --apikey [your api key]

For more information about making calls, please see the documentation.