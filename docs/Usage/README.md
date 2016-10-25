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

The following pictures need further description:


![MCellGalaxy](../images/01_first_data_set_details.png?raw=true "MCell in Galaxy")
![MCellGalaxy](../images/01_first_data_set_eye_view.png?raw=true "MCell in Galaxy")
![MCellGalaxy](../images/01_first_data_set.png?raw=true "MCell in Galaxy")
![MCellGalaxy](../images/01_show_data_model_tool.png?raw=true "MCell in Galaxy")
![MCellGalaxy](../images/02_modify_parameters_dr_2to3e4.png?raw=true "MCell in Galaxy")
![MCellGalaxy](../images/02_modify_parameters_empty.png?raw=true "MCell in Galaxy")
![MCellGalaxy](../images/02_show_data_model_details.png?raw=true "MCell in Galaxy")
![MCellGalaxy](../images/02_show_data_model_done.png?raw=true "MCell in Galaxy")
![MCellGalaxy](../images/02_show_data_model_eye_view.png?raw=true "MCell in Galaxy")
![MCellGalaxy](../images/03_modify_parameters_data_model.png?raw=true "MCell in Galaxy")
![MCellGalaxy](../images/03_modify_parameters_done.png?raw=true "MCell in Galaxy")
![MCellGalaxy](../images/03_modify_parameters_show_change.png?raw=true "MCell in Galaxy")
![MCellGalaxy](../images/04_data_model_to_mdl.png?raw=true "MCell in Galaxy")
![MCellGalaxy](../images/04_modify_parameters_details.png?raw=true "MCell in Galaxy")
![MCellGalaxy](../images/04_modify_parameters_show_done.png?raw=true "MCell in Galaxy")
![MCellGalaxy](../images/05_data_model_to_mdl_details.png?raw=true "MCell in Galaxy")
![MCellGalaxy](../images/05_data_model_to_mdl_done.png?raw=true "MCell in Galaxy")
![MCellGalaxy](../images/05_data_model_to_mdl_eye.png?raw=true "MCell in Galaxy")
![MCellGalaxy](../images/05_run_mcell_page.png?raw=true "MCell in Galaxy")
![MCellGalaxy](../images/10_gnu_plot_all_columns.png?raw=true "MCell in Galaxy")
![MCellGalaxy](../images/10_gnu_plot_setup.png?raw=true "MCell in Galaxy")
![MCellGalaxy](../images/10_mcell_result_eye.png?raw=true "MCell in Galaxy")
![MCellGalaxy](../images/10_mcell_result_tabular.png?raw=true "MCell in Galaxy")
![MCellGalaxy](../images/10_mcell_running.png?raw=true "MCell in Galaxy")
![MCellGalaxy](../images/11_gnu_plot_details.png?raw=true "MCell in Galaxy")
![MCellGalaxy](../images/11_gnu_plot_done.png?raw=true "MCell in Galaxy")
![MCellGalaxy](../images/11_gnu_plot_eye.png?raw=true "MCell in Galaxy")
![MCellGalaxy](../images/11_plot_mpl_blank.png?raw=true "MCell in Galaxy")
![MCellGalaxy](../images/11_plot_mpl_select_all.png?raw=true "MCell in Galaxy")
![MCellGalaxy](../images/12_plot_mpl_details.png?raw=true "MCell in Galaxy")
![MCellGalaxy](../images/12_plot_mpl.png?raw=true "MCell in Galaxy")
![MCellGalaxy](../images/12_plot_mpl_processing.png?raw=true "MCell in Galaxy")

