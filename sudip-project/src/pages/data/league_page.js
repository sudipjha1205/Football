import React from 'react';

import Attack from '../../components/attack';
import Defense from '../../components/defense';
import Goalie from '../../components/goalie';

import "./league_page.css";

const League_Page = (props) => {
    return(
        <div>
            <Attack league={props.league}/>
            <br/>
            <Defense league={props.league}/>
            <br />
            <Goalie league={props.league}/>
        </div>
    )
}

export default League_Page;