import ReactDOM from "react-dom";
import { ApolloProvider, ApolloClient, InMemoryCache } from "@apollo/client";

import App from "./App";

// for App_space
// const client = new ApolloClient({
//   uri: "https://api.spacex.land/graphql/",
//   cache: new InMemoryCache(),
// });

//for python backend
const client = new ApolloClient({
  uri: "http://0.0.0.0:8000/graphql",
  cache: new InMemoryCache(),
});

const rootElement = document.getElementById("root");
ReactDOM.render(
  <ApolloProvider client={client}>
    <App />
  </ApolloProvider>,
  rootElement
);
