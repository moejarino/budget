import { ApolloClient, InMemoryCache, ApolloProvider } from '@apollo/client'
import HomePage from './components/ui/HomePage'

// Create Apollo Client
const client = new ApolloClient({
  uri: import.meta.env.VITE_API_URL + '/graphql',
  cache: new InMemoryCache(),
})

function App() {
  return (
    <ApolloProvider client={client}>
      <HomePage />
    </ApolloProvider>
  )
}

export default App
