/* -*- Mode: rjsx -*- */

/*******************************************
 * Copyright (2018)
 *  Marcus Dillavou <line72@line72.net>
 *  http://line72.net
 *
 * Montclair:
 *  https://github.com/line72/montclair
 *  https://montclair.line72.net
 *
 * Licensed Under the GPLv3
 *******************************************/

import AvailtecParser from './AvailtecParser';

class Configuration {
    constructor() {
        // Mobile, AL
        this.center = [30.693707, -88.042476];

        this.agencies = [
            {
                name: 'Routes',
                parser: new AvailtecParser('https://realtimemobile.availtec.com/infopoint')
            }
        ];
    }
}

export default Configuration;
