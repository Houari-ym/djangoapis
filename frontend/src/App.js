import React from 'react';
import {Switch, Link, Route} from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';

import TodosList from './components/todos-list';
import AddTodos from './components/add-todos';
import Login from './components/login';
import Signup from './components/signup';

import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';

import Container from 'react-bootstrap/Navbar';

function App(){
  // const user=null;
  const[user, setUser]=React.useState(null); // this is just to preserve the state of the vars, ofred by react 
  const[token, setToken]=React.useState(null);
  const[error, setError]=React.userState("");


  async function login(user=null){setUser(user);}

  async function logout(){setUser(null);}

  async function signup(user=null){setUser(null)}


  return (
    <div className='App'>
      <Navbar bg="primary" variant="dark">
      <div className='container-fluid'>
        <Navbar.Brand>MeDev-TodoApp</Navbar.Brand>
        <Nav className="me-auto">
          <Container>
            <Link class="nav-link" to={"/todos"}>Todos</Link>
            { user ?(
              <Link class ="nav-link">Logout({user})</Link>
            ):(
              <>
              <Link class="nav-link" to={"/login"}>Login</Link>
              <Link class="nav-link" to={"/signup"}>Signup</Link>
              </>
            )}
          </Container>
        </Nav>
      </div>
      </Navbar>
    </div>
  )
}

export default App;