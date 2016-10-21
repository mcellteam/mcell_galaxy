# mcell_galaxy
Project to create an MCell tool that works within Galaxy

The files in this project may be copied on top of a fresh installation of Galaxy. Otherwise the files should be merged into a pre-existing Galaxy installation with the addition of an "mcell" section to the "galaxy/config/tool_conf.xml" file as shown here:


    <?xml version='1.0' encoding='utf-8'?>
    <toolbox monitor="true">
      <section id="mcell" name="MCell">
        <tool file="mcell/upload.xml" />
        <tool file="mcell/dm_to_mdl.xml" />
        <tool file="mcell/run_mcell_mdl.xml" />
        <tool file="mcell/run_mcell.xml" />
        <tool file="mcell/plot_gnu_simple.xml" />
        <tool file="mcell/plot_gnu_multiple.xml" />
        <tool file="mcell/plot_gnu.xml" />
        <tool file="mcell/test_cheetah.xml" />
      </section>

