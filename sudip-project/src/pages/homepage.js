import React from "react";
import "./homepage.css";

import datas from "../photos/datas.jpg";
import Matches from "./matches";
import Navbar from "../navbar";

const Homepage = () => {

    const top_scorer =[
        {pos:"1", player:"Erling Haaland", goals: "52"},
        {pos:"2", player:"Kylian Mbappe", goals:"40"},
        {pos:"3", player:"Robert lewandowski", goals:"32"},
        {pos:"4", player:"Harry Kane", goals:"30"},
        {pos:"5", player:"Alexandre Lacazette", goals:"30"},
        {pos:"6", player:"Marcus Rashford", goals:"29"},
        {pos:"7", player:"Mohammad Salah", goals:"29"},
        {pos:"8", player:"Karim Benzema", goals:"29"},
        {pos:"9", player:"Victor Osimhein", goals:"28"},
        {pos:"10", player:"Lautaro Martinez", goals:"25"}
    ]

    const goals_table = top_scorer.map((player) =>
        <tr>
        <th scope="row">{player.pos}</th>
        <td>{player.player}</td>
        <td>{player.goals}</td>
        </tr>
    )

    const top_player = [
        {pos:"1", player:"Lionel Messi", played:"30", rating:"8.31"},
        {pos:"2", player:"Kylian Mbappe", played:"30(2)", rating:"7.86"},
        {pos:"3", player:"Neymar", played:"18(2)", rating:"7.71"},
        {pos:"4", player:"Antoine Griezemann", played:"28(7)", rating:"7.64"},
        {pos:"5", player:"Kevin De Bruyne", played:"27(4)", rating:"7.62"},
        {pos:"6", player:"Jude Bellingham", played:"30(1)", rating:"7.58"},
        {pos:"7", player:"Karim Benzema", played:"22", rating:"7.57"},
        {pos:"8", player:"Erling Haaland", played:"32(2)", rating:"7.56"},
        {pos:"9", player:"Robert Lewandowski", played:"31(1)", rating:"7.49"},
        {pos:"10", player:"Joshua Kimmich", played:"31(1)", rating:"7.48"}
    ]

    const top_team = [
        {pos:"1",team:"Manchester City",ppg:"2.44",lstd:"1"},
        {pos:"2",team:"Napoli",ppg:"2.39",lstd:"1"},
        {pos:"3",team:"Barcelona",ppg:"2.36",lstd:"1"},
        {pos:"4",team:"Paris Saint Germain",ppg:"2.33",lstd:"1"},
        {pos:"5",team:"Arsenal",ppg:"2.19",lstd:"2"},
        {pos:"6",team:"Lens",ppg:"2.17",lstd:"2"},
        {pos:"7",team:"Dortmund",ppg:"2.12",lstd:"1"},
        {pos:"8",team:"Bayern Munich",ppg:"2.06",lstd:"2"},
        {pos:"9",team:"Atletico Madrid",ppg:"2.06",lstd:"2"},
        {pos:"10",team:"Real Madrid",ppg:"2.03",lstd:"3"},
    ]

    const top_assist = [
        {pos:"1", player:"Kevin De Bruyne", assists:"16"},
        {pos:"2", player:"Lionel Messi", assists:"16"},
        {pos:"3", player:"Antoine Griezmann", assists:"13"},
        {pos:"4", player:"Raphael Guerreiro", assists:"12"},
        {pos:"5", player:"Bukayo Saka", assists:"11"},
        {pos:"6", player:"Mohamed Salah", assists:"11"},
        {pos:"7", player:"Neymar", assists:"11"},
        {pos:"8", player:"Randal Kolo Muani", assists:"11"},
        {pos:"9", player:"Florian Kainz", assists:"10"},
        {pos:"10", player:"Jamal Musiala", assists:"10"}
    ]

    const assists_table = top_assist.map((player) =>
        <tr>
        <th scope="row">{player.pos}</th>
        <td>{player.player}</td>
        <td>{player.assists}</td>
        </tr>
    )

    const top_player_table = top_player.map((player) =>
        <tr>
        <th scope="row">{player.pos}</th>
        <td>{player.player}</td>
        <td>{player.played}</td>
        <td>{player.rating}</td>
        </tr>
    )

    const top_team_table = top_team.map((team) =>
        <tr>
        <th scope="row">{team.pos}</th>
        <td>{team.team}</td>
        <td>{team.ppg}</td>
        <td>{team.lstd}</td>
        </tr>
    )

    const premier_leage = [
        {time:"12:30",match:"Brighton vs Manchester City",venue:"Etihad"},
        {time:"12:30",match:"Manchester united vs Arsenal",venue:"Old Trafford"},
        {time:"1:30",match:"Leeds vs Everton",venue:"Ellan Road"}
    ]

    const la_liga = [
        {time:"7:30",match:"Valladolid vs Barcelona",venue:"Camp Nou"},
        {time:"10:30",match:"Real madrid vs Valencia",venue:"Mestella Stadium"},
        {time:"12:30",match:"Espanyol vs Athletic Bilbao",venue:"San Mames"}
    ]

    const serie_a = [
        {time:"8:30",match:"Roma vs Fiorentina",venue:"Roma"},
        {time:"12:30",match:"Inter vs AC Milan",venue:"San Siro"},
    ]

    const bundesliga = [
        {time:"6:30",match:"Hamburg vs RB Leipzig",venue:"Leipzig"},
        {time:"7:30",match:"Bayern Munich vs FC Koln",venue:"Allianz Arena"},
        {time:"7:30",match:"Dortmund vs FC Mainz",venue:"Signal Iduna Park"}
    ]

    const ligue1 = [
        {time:"12:30",match:"PSG vs Ajjacio",venue:"Parc De Princes"},
        {time:"12:30",match:"Lyon vs Lille",venue:"Groupama Stadium"},
        {time:"12:30",match:"Nice vs Toulouse",venue:"Stadium TFC"}
    ]

    const pl_matches = premier_leage.map((match) =>
        <tr>
        <th scope="row">{match.time}</th>
        <td class="text-center">{match.match}</td>
        <td class="text-end">{match.venue}</td>
        </tr>
    )

    const la_liga_matches = la_liga.map((match) =>
        <tr>
        <th scope="row">{match.time}</th>
        <td class="text-center">{match.match}</td>
        <td class="text-end">{match.venue}</td>
        </tr>
    )

    const bundesliga_matches = bundesliga.map((match) =>
        <tr>
        <th scope="row">{match.time}</th>
        <td class="text-center">{match.match}</td>
        <td class="text-end">{match.venue}</td>
        </tr>
    )

    const seriea_matches = serie_a.map((match) =>
        <tr>
        <th scope="row">{match.time}</th>
        <td class="text-center">{match.match}</td>
        <td class="text-end">{match.venue}</td>
        </tr>
    )

    const ligue1_matches = ligue1.map((match) =>
        <tr>
        <th scope="row">{match.time}</th>
        <td class="text-center">{match.match}</td>
        <td class="text-end">{match.venue}</td>
        </tr>
    )

    const leagues = [
        {league:"Premier League",function:pl_matches},
        {league:"La Liga",function:la_liga_matches},
        {league:"Serie A",function:seriea_matches},
        {league:"Bundesliga",function:bundesliga_matches},
        {league:"Ligue1",function:ligue1_matches}
    ]

    const league_table = leagues.map((league) =>
        <table class="table table-secondary table-hover">
            <thead>
                <tr>
                <th scope="col"></th>
                <th scope="col" class="d-flex justify-content-center">{league.league}</th>
                <th scope="col"></th>
                </tr>
            </thead>
            <tbody>
                {league.function}
            </tbody>
        </table> 
    )


    return(
        <div>
            <Navbar />
            <div class="container-fluid">
                <div class="col-12 row m-0 p-0 d-flex h-80">
                    <div class="col-md-3">
                        <div class="badge bg-secondary text-wrap fs-4 m-1 p-1.5 b-2 d-flex justify-content-center">Most Goals Scored</div>
                        <table class="table table-secondary table-hover">
                            <thead>
                                <tr>
                                <th scope="col">#</th>
                                <th scope="col">Player</th>
                                <th scope="col">Goals</th>
                                </tr>
                            </thead>
                            <tbody>
                                {goals_table}
                            </tbody>
                        </table>
                        <div class="badge bg-secondary text-wrap fs-4 m-1 p-1.5 b-2 d-flex justify-content-center">Most Assists</div>
                        <table class="table table-secondary table-hover">
                            <thead>
                                <tr>
                                <th scope="col">#</th>
                                <th scope="col">Player</th>
                                <th scope="col">Assists</th>
                                </tr>
                            </thead>
                            <tbody>
                                {assists_table}
                            </tbody>
                        </table>
                    </div>
                    <div class='col-md-6'>
                        <div class="badge bg-secondary text-wrap fs-4 m-1 p-1.5 d-flex justify-content-center">Matches</div>
                        <Matches />
                        <Matches />
                        <Matches />
                        <Matches />
                        <Matches />
                    </div>
                    <div class="col-md-3">
                        <div class="badge bg-secondary fs-4 text-wrap m-1 p-1.5 d-flex justify-content-center">Player's Rating</div>
                        <table class="table table-secondary table-hover">
                            <thead>
                                <tr>
                                <th scope="col">#</th>
                                <th scope="col">Player</th>
                                <th scope="col">Played</th>
                                <th scope="col">Rating</th>
                                </tr>
                            </thead>
                            <tbody>
                                {top_player_table}
                            </tbody>
                        </table>
                        <div class="badge bg-secondary fs-4 text-wrap m-1 p-1.5 d-flex justify-content-center">Team Rating</div>
                        <table class="table table-secondary table-hover">
                            <thead>
                                <tr>
                                <th scope="col">#</th>
                                <th scope="col">Team</th>
                                <th scope="col">PPG</th>
                                <th scope="col">L.STD</th>
                                </tr>
                            </thead>
                            <tbody>
                                {top_team_table}
                            </tbody>
                        </table>
                        <p class="text-light fw-lighter">*PPG - Points per game. *L.STD - Respective League Standing</p>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Homepage;