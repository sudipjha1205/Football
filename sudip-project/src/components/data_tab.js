import React from 'react';
import "./data_tab.css";
import League_Page from '../pages/data/league_page';
import Fixtures from './fixtures';

const Data_Tab = () => {
    return(
           <div>
                <nav>
                    <div class="nav nav-tabs justify-content-center" id="nav-tab" role="tablist">
                        <button class="nav-link active" id="nav-top-5-tab" data-bs-toggle="tab" data-bs-target="#nav-top-5" type="button" role="tab" aria-controls="nav-top-5" aria-selected="true">Top 5 League</button>
                        <button class="nav-link" id="nav-premier-league-tab" data-bs-toggle="tab" data-bs-target="#nav-premier-league" type="button" role="tab" aria-controls="nav-premier-league" aria-selected="false">Premier League</button>
                        <button class="nav-link" id="nav-la-liga-tab" data-bs-toggle="tab" data-bs-target="#nav-la-liga" type="button" role="tab" aria-controls="nav-la-liga" aria-selected="false">La Liga</button>
                        <button class="nav-link" id="nav-serie-a-tab" data-bs-toggle="tab" data-bs-target="#nav-serie-a" type="button" role="tab" aria-controls="nav-serie-a" aria-selected="false">Serie A</button>
                        <button class="nav-link" id="nav-ligue-1-tab" data-bs-toggle="tab" data-bs-target="#nav-ligue-1" type="button" role="tab" aria-controls="nav-ligue-1" aria-selected="false">Ligue 1</button>
                        <button class="nav-link" id="nav-bundesliga-tab" data-bs-toggle="tab" data-bs-target="#nav-bundesliga" type="button" role="tab" aria-controls="nav-bundesliga" aria-selected="false">Bundesliga</button>
                    </div>
                    </nav>
                    <div class="tab-content" id="nav-tabContent">
                        <div class="tab-pane fade show active" id="nav-top-5" role="tabpanel" aria-labelledby="nav-top-5-tab"><Fixtures /></div>
                        <div class="tab-pane fade" id="nav-premier-league" role="tabpanel" aria-labelledby="nav-premier-league-tab"><Fixtures /></div>
                        <div class="tab-pane fade" id="nav-la-liga" role="tabpanel" aria-labelledby="nav-la-liga-tab"><Fixtures /></div>
                        <div class="tab-pane fade" id="nav-serie-a" role="tabpanel" aria-labelledby="nav-serie-a-tab"><Fixtures /></div>
                        <div class="tab-pane fade" id="nav-ligue-1" role="tabpanel" aria-labelledby="nav-ligue-1-tab"><Fixtures /></div>
                        <div class="tab-pane fade" id="nav-bundesliga" role="tabpanel" aria-labelledby="nav-bundesliga-tab"><Fixtures /></div>
                    </div>
            </div>
    )
}

export default Data_Tab;