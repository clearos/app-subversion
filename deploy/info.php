<?php

/////////////////////////////////////////////////////////////////////////////
// General information
/////////////////////////////////////////////////////////////////////////////

$app['basename'] = 'subversion';
$app['version'] = '1.5.0';
$app['release'] = '2';
$app['vendor'] = 'ClearFoundation';
$app['packager'] = 'ClearFoundation';
$app['license'] = 'GPLv3';
$app['license_core'] = 'LGPLv3';
$app['description'] = lang('subversion_app_description');

/////////////////////////////////////////////////////////////////////////////
// App name and categories
/////////////////////////////////////////////////////////////////////////////

$app['name'] = lang('subversion_app_name');
$app['category'] = lang('base_category_server');
$app['subcategory'] = 'Developer'; // e.g. lang('base_subcategory_settings');
$app['menu_enabled'] = FALSE;

/////////////////////////////////////////////////////////////////////////////
// Packaging
/////////////////////////////////////////////////////////////////////////////

$app['core_only'] = TRUE;

$app['core_requires'] = array(
    'app-storage-core',
    'subversion',
);

$app['core_directory_manifest'] = array(
    '/var/clearos/subversion' => array(),
    '/var/clearos/subversion/repositories' => array(),
);

$app['core_file_manifest'] = array(
    'subversion_default.conf' => array ('target' => '/etc/clearos/storage.d/subversion_default.conf'),
);
