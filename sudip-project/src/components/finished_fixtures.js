import React from 'react';
import { useState, useEffect } from 'react';

const FinishedFixtures = () => {

    const [finishedFixtures, setFinishedFixtures] = useState([])

    useEffect(() => {
        fetch('http://127.0.0.1:8000/api/fixtures/finished/',{
            method:'POST',
            headers:{
                'Content-Type':'application/json',
            },
            body:JSON.stringify({"League_name":"Premier League"})
        })
        .then((response) => response.json())
        .then((data) => setFinishedFixtures(data))
    },[])

    const fixtures = finishedFixtures && finishedFixtures.map((fixture) => {
        const timestamp = fixture.timestamp
        const date = new Date(fixture.fixture_date)

        const localDate = date.toLocaleString();
        console.log(date)

        return(
        <tr>
            <th scope='row'>{localDate}</th>
            <td>{fixture.fixture_venue_name}</td>
            <td>{fixture.teams_home_name}</td>
            <td>{fixture.goals_home} - {fixture.goals_away}</td>
            <td>{fixture.teams_away_name}</td>
        </tr>
    )})

    return(
        <div>
            <div class='container pt-4 pb-4'>
                <div class='table-style'>
                    <table class="table table-secondary border-bottom border-rounded border-0.5 border-light table-hover fw-light">
                        <thead>
                            <tr>
                                <th scope='col'>Time</th>
                                <th scope='col'>Venue</th>
                                <th scope='col'>Home</th>
                                <th scope='col'>Score</th>
                                <th scope='col'>Away</th>
                            </tr>
                        </thead>
                        <tbody>
                            {fixtures}
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    )
}

export default FinishedFixtures;