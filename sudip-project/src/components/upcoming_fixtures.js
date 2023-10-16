import React from 'react';
import { useState, useEffect } from 'react';

const UpcomingFixtures = () => {

    const [upcomingFixtures, setUpcomingFixtures] = useState([])

    useEffect(() => {
        fetch('http://127.0.0.1:8000/api/fixtures/upcoming/',{
            method:'POST',
            headers:{
                'Content-Type':'application/json',
            },
            body:JSON.stringify({"League_name":"Premier League"})
        })
        .then((response) => response.json())
        .then((data) => console.log(data))
    },[])
}

export default UpcomingFixtures;