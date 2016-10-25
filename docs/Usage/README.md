# MCell Galaxy

## Galaxy tools to run MCell within Galaxy

This suite of tools supports uploading of MCell/CellBlender data models, 
modification of parameters within models, exporting data models to MDL,
running MCell on exported MDL, plotting results in GnuPlot and MatPlotLib.

When properly installed, the home page of Galaxy should look like this:

![MCellGalaxy](../images/00_front_page.png?raw=true "MCell running in Galaxy")

The default layout for Galaxy shows three panels:

1. Tools on the left
2. Work area in the center
3. Data sets and data set history on the right

In this picture, the "MCell" tool group has been opened in the left (tools) panel:

![MCellGalaxy](../images/00_mcell_open.png?raw=true "MCell in Galaxy")

You can see these tools within the MCell tool group:

* Upload File
* Show Data Model
* Modify Parameters
* Data Model to MDL
* Run MCell MDL
* Gnu Plot Multiple
* Plot MPL

Each tool (with the exception of "Upload") uses a Galaxy data set as its input.
Similarly, each tool produces a Galaxy data set as its output. Note that Galaxy
data sets have "types" associated with them. The tools are designed to accept only
compatible input data sets. However, some "types" can be used at multiple points
and with multiple tools in a process so it's important to keep track of data by naming it.
The following tutorial will walk through that process. Note that this tutorial starts
with a CellBlender data model and eventually produces MDL files. Some of these steps can
be skipped by uploading an MDL file directly (use **Galaxy's Get Data / Upload File** and
specify a type of "txt" to upload raw MDL files).

We will start by uploading a JSON data model from CellBlender. Use the "Upload File" option
shown in the MCell tool group. That will pop open a window allowing you to select (or drag
and drop) a JSON data model into Galaxy:


![MCellGalaxy](../images/00_upload_json_data_model.png?raw=true "MCell in Galaxy")

After the upload completes, you will see the new data set in green on the right side panel:

![MCellGalaxy](../images/01_first_data_set.png?raw=true "MCell in Galaxy")

In this case, it gives the file name ("Release_Decay.json") and its data set number (1).
There are also a number of controls shown, and we'll describe some of them next. The first of
these is simply clicking on the data set name ("Release_Decay.json") which will expand the green
data set panel to show more details:

![MCellGalaxy](../images/01_first_data_set_details.png?raw=true "MCell in Galaxy")

To show the file itself, you can click on the "eye" icon ("View data"). This will fill the
center panel with a view of that data set. In this case, the file contains JSON (without
line breaks), and the default display is just the text without any wrapping (note the line
of text across the top of the center panel):

![MCellGalaxy](../images/01_first_data_set_eye_view.png?raw=true "MCell in Galaxy")

Since this "raw" view of the JSON data model isn't particularly helpful, the The MCell
Galaxy tool section also contains a "Show Data Model" tool which will format the data and
produce an HTML output file which Galaxy can display. Click on the "Show Data Model" tool,
and it will bring up a tool view in the center panel that looks like this:

![MCellGalaxy](../images/01_show_data_model_tool.png?raw=true "MCell in Galaxy")

This is the standard Galaxy tool interface, and you'll notice a number of controls in
the center panel. One of the most important controls is the data set being operated on. In this
case it's titled "JSON data model to display", and it contains a drop down selection box.
That box chooses from among the data sets that are in the "History" panel (on the right).
At this point, the only history is our uploaded JSON file ("Release_Decay.json") and that's
what is selected by default. Each tool knows what types of data set it can use, and it will
select (by default) the most recent data set appropriate for that tool. You'll see how that
makes things easier as we continue to add new datasets in the Galaxy workflow. For now, click
the "Execute" button and that will run the "Show Data Model" tool. When it's finished, you
should see that the job has been queued and it should show this result:

![MCellGalaxy](../images/02_show_data_model_done.png?raw=true "MCell in Galaxy")

As before, we can click on the data set name ("2: Show Data Model on data 1") to see more details
in the right (green) panel:

![MCellGalaxy](../images/02_show_data_model_details.png?raw=true "MCell in Galaxy")

This expands the green section to show a little more about the data set. For example, we can
see that this data set is 15.1KB in "html" format. To see the actual results, click the "View data" 
(eye button) to see the HTML page rendered in the center panel:

![MCellGalaxy](../images/02_show_data_model_eye_view.png?raw=true "MCell in Galaxy")

This is an HTML rendering of the data model file that we uploaded. Since this tool is geared
toward running MCell simulations, the available parameters have been displayed at the top. These
are the things we can change in this particular model. The HTML page also shows the "raw" JSON
Data Model below the parameters. This is a slightly better format than the Galaxy default of a
single line shown earlier.

We could run this model just as it is, but we'll change one of the parameters first while we're
looking at them. This current MCell/Galaxy tool doesn't have a mechanism to change parameters
from the HTML display, so we'll use another tool (in the left panel) called "Modify Parameters".
But before we do that, we should note which parameter it is that we want to change and what new
value we want to use. For our example, we'll change the "Decay Reaction Rate" (dr in the second row)
from its current value of 2e4 to a new value of 3e4. Once we've made that note, we can click on the
"Modify Parameters" tool which brings up the following page:

![MCellGalaxy](../images/02_modify_parameters_empty.png?raw=true "MCell in Galaxy")

As usual, the first item in that page is the data set that we're going to operate on. This is
our "Release_Decay.json" file that we've been using. Notice that because this tool expects to
use a JSON file, the default is our first set (which is JSON) and NOT our second set (which is
HTML). In order to modify a parameter with this tool we need to use the "Insert MCell Parameters
to Modify" (+) button. Clicking that button will add a new name/value pair to the list. You should
type the name ("dr") in the "Parameter Name" field, and type "3e4" in the "Parameter Value" field.
You could change additional parameter fields at this time by using the "Insert..." button as many
times as needed. For now, we'll just make that one change as shown here:

![MCellGalaxy](../images/02_modify_parameters_dr_2to3e4.png?raw=true "MCell in Galaxy")

When we press "Execute" it will again run the job and show us a completed result and the new
data set ("3: Modify Parameters on data 1") will appear in the history panel on the right in
the history panel:

![MCellGalaxy](../images/03_modify_parameters_done.png?raw=true "MCell in Galaxy")

As before, we can click on the various controls to view our data. In this case the data set name has
been clicked which shows the expanded information here:

![MCellGalaxy](../images/03_modify_parameters_data_model.png?raw=true "MCell in Galaxy")

If we want to see the HTML display with our newly changed value, we can again run the "Show Data Model"
tool on the newly created data set. Click on the "Show Data Model" item in the left panel to show this:

![MCellGalaxy](../images/03_modify_parameters_show_change.png?raw=true "MCell in Galaxy")

As before, the default data set will be the most recent one from the history that fits with this
tool. Since this tool displays a JSON data model, it will select history item 3 because it's a
JSON data set and it is more recent than our original JSON file (history item 1). If we click the
"Execute" button, it will again generate an HTML data set (number 4 this time) showing the parameters
and complete data model from this most recent JSON file.

![MCellGalaxy](../images/04_modify_parameters_show_done.png?raw=true "MCell in Galaxy")

As before, the newly created data set is added to the top of the history stack. This one is shown
as number 4 in this particular history. As before, we can click on the data set name in the right
(green) panel to show more details:

![MCellGalaxy](../images/04_modify_parameters_details.png?raw=true "MCell in Galaxy")

As before, the "Show Data Model" tool has produced an HTML file of about 15KB. We can also click on 
the "eye" icon to see the data set itself. You'll note that the previous value of 1e4 has been changed
to 30000.0 (which is 3e4).

![MCellGalaxy](../images/04_show_data_set_html.png?raw=true "MCell in Galaxy")

This shows that we've been able to change one of the parameters in the data model. This change
(and all of our work so far) is stored in the Galaxy history panel on the right.

Now let's run the model in MCell. The current workflow requires that we convert the data model
representation (JSON) into MCell's Model Description Language (MDL). The MCell/Galaxy tool group
has a tool named "Data Model to MDL" designed for this task. When you select that tool, it will
display another data set selection control in the center panel. As usual, it will have selected
the most recent data set consistent with the tool. Since this tool expects JSON, it will default
to our most recently created JSON data set which is the one we created by modifying the "dr" parameter:

![MCellGalaxy](../images/04_data_model_to_mdl.png?raw=true "MCell in Galaxy")

Click the "Execute" button to perform the conversion. You will see this new data set added to the
top of the history panel (on the right). In this example it is number "5" titled "5: Data Model to MDL
on data 3" which reflects its history:

![MCellGalaxy](../images/05_data_model_to_mdl_done.png?raw=true "MCell in Galaxy")
 
As usual, we can click the data set name to show more information about the results. In this case it
will show the output is "txt" format containing 118 lines. This is the appropriate format for MDL since
there is no built-in representation for MDL files in Galaxy.

![MCellGalaxy](../images/05_data_model_to_mdl_details.png?raw=true "MCell in Galaxy")

If we want to see the MDL itself, we can again use the "eye" button and it will display the MDL text
in the center panel:

![MCellGalaxy](../images/05_data_model_to_mdl_eye.png?raw=true "MCell in Galaxy")

Now we're ready to run MCell itself on the MDL file. The MCell tool group (left side) contains an item
named "Run MCell MDL". Click on that item and it should show the MCell running page:

![MCellGalaxy](../images/05_run_mcell_page.png?raw=true "MCell in Galaxy")

Once again, it has guessed at the most recent (and compatible) data set to use for input. Since it's
looking for a text (MDL) file, the most recent item in the history is "5: Data Model to MDL on data 3",
and that's what is selected in the "MDL file to run" field.

The MCell run tool also contains an option seed that can be run. Changing the "Select a seed" field from
"No" to "Yes" would bring up an additional field for setting the seed. It's not needed in this case,
and we can use the default. Click the "Execute" button to start running, and you should see the job
submission status along with the yellow "job in progress" panel on the right. Note that in this example,
the history item is shown as item "10" rather than the expected "6". That reflects several "trial and error"
runs during the construction of this tutuorial. The Galaxy history makes it easy to delete data sets that
didn't work out and run them again.

![MCellGalaxy](../images/10_mcell_running.png?raw=true "MCell in Galaxy")

Once the MCell is done running, the data set item (10 in this example) will turn green, and you'll see
that it contains 501 lines of "tabular" data (click the data set name to show this).

![MCellGalaxy](../images/10_mcell_result_tabular.png?raw=true "MCell in Galaxy")

As usual, we can use the "eye" button to show the actual data. Click it and you'll see these 4 columns
which represent time (on the left) and the counts of the 3 different molecules in the simulation (columns
2, 3, and 4).

![MCellGalaxy](../images/10_mcell_result_eye.png?raw=true "MCell in Galaxy")

Now let's use GnuPlot to plot these 3 data columns as a function of time. Click the "GNU Plot Multiple"
tool item in the left panel to show the plotting panel in the center:

![MCellGalaxy](../images/10_gnu_plot_setup.png?raw=true "MCell in Galaxy")

This tool allows selection of individual columns. For now, click the "Select/Unselect All" check box
so that it shows all of the columns:

![MCellGalaxy](../images/10_gnu_plot_all_columns.png?raw=true "MCell in Galaxy")

Then click the "Execute" button to run the plotting job. It will show when it is done:

![MCellGalaxy](../images/11_gnu_plot_done.png?raw=true "MCell in Galaxy")

As before, we can click the data set name (green panel) to show more details. In this case, we see that the 
result "11: GNU Plot Multiple on data 10" data set has been created. It is 4.6KB in size and is a "png" image
format.

![MCellGalaxy](../images/11_gnu_plot_details.png?raw=true "MCell in Galaxy")

We can again click on the "eye" button to view the data and it should show the PNG file created by GnuPlot:

![MCellGalaxy](../images/11_gnu_plot_eye.png?raw=true "MCell in Galaxy")

GnuPlot does a pretty good job, but Galaxy is not limited to any one plotting package. For example, the
MCell tool group also contains a MatPlotLib plotter named "Plot MPL". If you click the "Plot MPL" tool,
it will bring up this panel in the center:

![MCellGalaxy](../images/11_plot_mpl_blank.png?raw=true "MCell in Galaxy")

There are a number of features (many of which are still under development), but you can select a data set
and choose to show all columns just as you did with the GnuPlot tool:

![MCellGalaxy](../images/11_plot_mpl_select_all.png?raw=true "MCell in Galaxy")

Click the "Execute" button, and you'll again see the familiar yellow "processing" panel as it builds the
resulting data set:

![MCellGalaxy](../images/12_plot_mpl_processing.png?raw=true "MCell in Galaxy")

When it's done, you can again click on the data set name to show that this tool also produces a PNG file,
and in this example it is 33.7KB in size.

![MCellGalaxy](../images/12_plot_mpl_details.png?raw=true "MCell in Galaxy")

You can also click the "eye" button to show the actual results which should be a plot similar to the
GnuPlot version:

![MCellGalaxy](../images/12_plot_mpl.png?raw=true "MCell in Galaxy")



