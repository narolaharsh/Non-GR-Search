cat <<END_OF_TEXT
<?xml version="1.0" encoding="UTF-8"?>
<sitecatalog xmlns="http://pegasus.isi.edu/schema/sitecatalog" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xsi:schemaLocation="http://pegasus.isi.edu/schema/sitecatalog http://pegasus.isi.edu/schema/sc-4.0.xsd" version="4.0">
  <site handle="local" arch="x86_64" os="LINUX">
    <directory  path="${LOCAL_SITE_SCRATCH_PATH}/local-site-scratch" type="shared-scratch" free-size="null" total-size="null">
        <file-server  operation="all" url="${LOCAL_SITE_SCRATCH_URL}/local-site-scratch">
        </file-server>
    </directory>
    <directory  path="${LOCAL_SITE_STORAGE_PATH}" type="shared-storage" free-size="null" total-size="null">
        <file-server  operation="all" url="${LOCAL_SITE_STORAGE_URL}">
        </file-server>
    </directory>
    <profile namespace="pegasus" key="style">condor</profile>
    <profile namespace="condor" key="getenv">True</profile>
    <profile namespace="condor" key="should_transfer_files">YES</profile>
    <profile namespace="condor" key="when_to_transfer_output">ON_EXIT_OR_EVICT</profile>
    <profile namespace="condor" key="+DESIRED_Sites">&quot;nogrid&quot;</profile>
    <profile namespace="condor" key="+IS_GLIDEIN">&quot;False&quot;</profile>
    <profile namespace="condor" key="accounting_group">ligo.sim.o2.cbc.explore.test</profile>
    <profile namespace="condor" key="accounting_group_user"></profile>
    <profile namespace="condor" key="use_x509userproxy">True</profile>
  </site>
</sitecatalog>
END_OF_TEXT
