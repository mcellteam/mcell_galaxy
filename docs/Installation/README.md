# MCell Galaxy

## Installation Details

The files in this project may be copied on top of a fresh installation of Galaxy. 
Otherwise the files should be merged into a pre-existing Galaxy installation with 
the addition of an "mcell" section added to the "galaxy/config/tool_conf.xml" file 
as shown here:

    <?xml version='1.0' encoding='utf-8'?>
    <toolbox monitor="true">
      <section id="mcell" name="MCell">
        <tool file="mcell/upload.xml" />
        <tool file="mcell/show_dm.xml" />
        <tool file="mcell/modify_dm_parameters.xml" />
        <tool file="mcell/dm_to_mdl.xml" />
        <tool file="mcell/run_mcell_mdl.xml" />
        <tool file="mcell/plot_mpl.xml" />
        <tool file="mcell/plot_gnu_multiple.xml" />
      </section>


In order to run MCell itself, the mcell executable must be placed in the 
galaxy/tools/mcell directory. A recent version is currently stored in the 
repository for convenience.
