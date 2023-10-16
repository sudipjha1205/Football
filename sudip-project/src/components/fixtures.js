import React from 'react';
import {useState,useEffect} from 'react';

import Standings from './standings';
import FinishedFixtures from './finished_fixtures';
import League_Page from '../pages/data/league_page';

import './fixtures.css';

const Fixtures = () => {
    return(
        <div class='fixtures'>
            <div className='container pt-3 pb-4 border border-0'> 
                <ul class="nav nav-tabs" id="myTab" role="tablist">
                    <li class="nav-item" role="presentation">
                        <button class="nav-link" id="standings-tab" data-bs-toggle="tab" data-bs-target="#Standings" type="button" role="tab" aria-controls="home" aria-selected="true">Standings</button>
                    </li>
                    <li class="nav-item" role="presentation">
                        <button class="nav-link" id="results-tab" data-bs-toggle="tab" data-bs-target="#Results" type="button" role="tab" aria-controls="profile" aria-selected="false">Results</button>
                    </li>
                    <li class="nav-item" role="presentation">
                        <button class="nav-link" id="fixtures-tab" data-bs-toggle="tab" data-bs-target="#Fixtures" type="button" role="tab" aria-controls="contact" aria-selected="false">Fixtures</button>
                    </li>
                    <li class="nav-item" role="presentation">
                        <button class="nav-link" id="live-tab" data-bs-toggle="tab" data-bs-target="#Live" type="button" role="tab" aria-controls="contact" aria-selected="false">Live</button>
                    </li>
                    <li class="nav-item" role="presentation">
                        <button class="nav-link" id="stats-tab" data-bs-toggle="tab" data-bs-target="#Stats" type="button" role="tab" aria-controls="contact" aria-selected="false">Stats</button>
                    </li>
                    <li class="nav-item" role="presentation">
                        <button class="nav-link" id="analytics-tab" data-bs-toggle="tab" data-bs-target="#Analytics" type="button" role="tab" aria-controls="contact" aria-selected="false">Analytics</button>
                    </li>
                </ul>
                <div class="tab-content" id="myTabContent">
                    <div class="tab-pane fade show active" id="Standings" role="tabpanel" aria-labelledby="standings-tab"><Standings /></div>
                    <div class="tab-pane fade" id="Results" role="tabpanel" aria-labelledby="finishedfixtures-tab"><FinishedFixtures /></div>
                    <div class="tab-pane fade" id="Fixtures" role="tabpanel" aria-labelledby="fixtures-tab"><FinishedFixtures /></div>
                    <div class="tab-pane fade" id="Live" role="tabpanel" aria-labelledby="live-tab">Live</div>
                    <div class="tab-pane fade" id="Stats" role="tabpanel" aria-labelledby="stats-tab"><League_Page league='premier_league' /></div>
                    <div class="tab-pane fade" id="Analytics" role="tabpanel" aria-labelledby="analytics-tab">Analytics</div>
                </div>
            </div>
        </div>
    )
}

export default Fixtures;