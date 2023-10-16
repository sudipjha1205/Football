import React from 'react';
import { useEffect,useState } from 'react';

import UpcomingFixtures from './upcoming_fixtures';

const Standings = (props) => {

    const [standings, setStandings] = useState([]);

    useEffect(() => {
        fetch('http://127.0.0.1:8000/api/premier_league/standings/')
        .then((response) => response.json())
        .then((data) => {
            setStandings(data);
        })
    },[]);

    const standings_table = standings && standings.map((team) => 
        <tr>
        <th scope="row">{team.rank}</th>
        <td>{team.team_name}</td>
        <td>{team.all_played}</td>
        <td>{team.all_win}</td>
        <td>{team.all_draw}</td>
        <td>{team.all_lose}</td>
        <td>{team.all_goals_for}</td>
        <td>{team.all_goals_against}</td>
        <td>{team.goals_diff}</td>
        <td>{team.points}</td>
        <td>{team.form}</td>
        </tr>
    )

    return(
        <div>
            <div class="container pt-4 pb-4">
                <div class="table-style">
                    <table class="table table-secondary border-bottom border-rounded border-0.5 border-light table-hover fw-light">
                        <thead>
                            <tr>
                            <th scope="col">Rank</th>
                            <th scope="col">Club</th>
                            <th scope="col">Played</th>
                            <th scope="col">Won</th>
                            <th scope="col">Drawn</th>
                            <th scope="col">Lose</th>
                            <th scope="col">GF</th>
                            <th scope="col">GA</th>
                            <th scope="col">GD</th>
                            <th scope="col">Points</th>
                            <th scope="col">Form</th>
                            </tr>
                        </thead>
                        <tbody>
                            {standings_table}
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    )
}


export default Standings;