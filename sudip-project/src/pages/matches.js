import React from 'react';
import { useEffect, useState } from 'react';

import './matches.css';

const Matches = () => {
    const [matchweek,setMatchweek] = useState('')
    const [matches,setMatches] = useState([])
    const [league,setLeague] = useState('')

    const getSeasonRound = async () => {
        const response = await fetch('https://api-football-v1.p.rapidapi.com/v3/fixtures/rounds?league=39&season=2023&current=true',{
	method: 'GET',
	headers: {
		'X-RapidAPI-Key': '627a6337camsh8c2abad82cd70f7p12c64ajsn4f840c2e3905',
		'X-RapidAPI-Host': 'api-football-v1.p.rapidapi.com'
	}
    })
    .then(response => response.json())
	.catch(err => console.error(err));

    setMatchweek(response['response']);
    };

    const getMatches = async () => {
        const response = await fetch('https://api-football-v1.p.rapidapi.com/v3/fixtures?league=39&season=2023&round=Regular%20Season%20-%2038',{
            method: 'GET',
	        headers: {
		        'X-RapidAPI-Key': '627a6337camsh8c2abad82cd70f7p12c64ajsn4f840c2e3905',
		        'X-RapidAPI-Host': 'api-football-v1.p.rapidapi.com'
            }
        })
        .then(response => response.json())
        .catch(err => console.error(err));

        setMatches(response['response']);
        setLeague(response['response'][0]['league']['name'])
    }

    useEffect(() => {
        getMatches();
    },[]);

    useEffect(() => {
        getSeasonRound();
    },[])

    return(
        <div>
            <table class="table table-secondary table-hover">
            <thead>
                <tr>
                <th scope="col"></th>
                <th scope="col" class="d-flex justify-content-center">{league}</th>
                <th scope="col"></th>
                </tr>
            </thead>
            <tbody>
                {matches && matches.map(match => 
                <tr>
                <th scope="row">{match['fixture']['date']}</th>
                <td class="text-center">{match['teams']['home']['name']} VS {match['teams']['away']['name']}</td>
                <td class="text-end">{match['fixture']['venue']['name']}</td>
                </tr>
                )}
            </tbody>
        </table> 
        </div>
    )
}

export default Matches;