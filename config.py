# -*- mode: python -*-

import transmogrifier

CONFIG = transmogrifier.Config(
    build_dir = './build',
    repo = 'mobile',
    package_name = 'montclair-mobile',
    name = 'Go Mobile',
    description = 'Real Time Tracking of the Buses for Mobile, AL',
    url = 'https://mobile.gotransitapp.com',
    logo_svg = 'assets/logo.svg',
    montclair_config = transmogrifier.MontclairConfig(
        version = '1.6.0',
        revision = 2,
        title = 'Go Mobile',
        first_run_text = "Welcome to Mobile, AL's Real Time Bus Tracker.<br /><br />Please select one or more routes to begin!",
        configuration_js_file = 'assets/Configuration.js'
    ),
    ios_config = transmogrifier.MontclairiOSConfig(
        version = '2.0.4',
        revision = 1,
        app_id = 'com.gotransitapp.mobile',
        app_store_id = '1493405198',
        app_store_url = 'https://apps.apple.com/us/app/go-mobile-al/id1493405198'
    ),
    android_config = transmogrifier.MontclairAndroidConfig(
        version = '1.0.2',
        revision = 1,
        app_id = 'com.gotransitapp.mobile',
        play_store_url = 'https://play.google.com/store/apps/details?id=com.gotransitapp.mobile'
    )
)
