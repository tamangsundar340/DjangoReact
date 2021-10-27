import React from 'react';
import ReactDOM from 'react-dom';
import {
  BrowserRouter as Router,
  Switch,
  Route,
} from "react-router-dom";

// components of client site
import Layout from './Client/hocs/Layout'
import MainComponent from './Client/Component/MainComponent';
import Blog from './Client/Pages/Blog';
import BlogDetail from './Client/Pages/BlogDetail';
import Youtube from './Client/Pages/Youtube';
import Contact from './Client/Pages/Contact';
import Category from './Client/Pages/Category';
import VideoList from './Client/Pages/VideoList'
import SingleVideo from './Client/Pages/SingleVideo';

ReactDOM.render(
  <Router>
    <Layout>
      <Switch>
        <Route exact path="/" component={MainComponent} />
        <Route exact path="/blog" component={Blog} />
        <Route exact path="/blog/:id" component={BlogDetail} />
        <Route exact path="/category/:id" component={Category} />
        <Route exact path="/youtube" component={Youtube} />
        <Route exact path="/videolist/:id" component={VideoList} />
        <Route exact path="/video/:id" component={SingleVideo} />
        <Route exact path="/contact" component={Contact} />
      </Switch>
    </Layout>
  </Router>,
  document.getElementById('root')
);
