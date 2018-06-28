Syngenta CKAN Extension
=========================

Step 1:

* Activate your virtual environment; use the path to your virtual environment. On Mac OSX, you may have to use `/usr/local/lib/ckan/default/bin/activate`. You can copy the code as it is below, including the preceeding dot.
```
. /usr/lib/ckan/default/bin/activate
```

Step 2:

* Install the extension

If you are not a developer and just want to install the extension from package, just run this command from your virtual environment:
```
pip install ckanext-syngenta
```
> **Note**: If you wish to modify the extension in any way, you can download the source code and install the extension manually. To do so, execute the following command:
> ```
> $ pip install -e git+https://github.com/<update>/ckanext-syngenta.git#egg=ckanext-syngenta
> ```
> **Alternatively**: You can clone this repo (preferrably into the /src directory where you installed CKAN), cd into ckanext-syngenta and run
> ```
> $ python setup.py develop
> ```

Step 3:

* Modify your configuration file (generally in `/etc/ckan/default/production.ini`) and add `syngenta` in the `ckan.plugins` property.
```
ckan.plugins = syngenta <OTHER_PLUGINS>
```

Step 4: 

* Restart your server:

```
paster serve /etc/ckan/default/production.ini
```
OR
```
paster serve --reload /etc/ckan/default/production.ini
```
With `--reload`, your server is restarted automatically whenever you make changes in your source code.

If your extension is installed successfully, your page will change to the syngenta theme.

**Note**: This extension, being a thememing extension, may override templates from other extensions. Templates in /ckanext/syngenta/templates 
may require some modifications to render properly with syngenta extension.

