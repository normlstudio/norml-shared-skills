# Runtime registration

An MCP install, handshake, OAuth grant, target-resource read and live operation
are different stages. Check each independently in the intended runtime/profile.
Inspect supported CLI help before registration and preserve unrelated entries.
Use the provider’s approved authentication method and a protected credential
store; do not export another runtime’s OAuth tokens.

Remote OAuth connectors and local unauthenticated loopback editors have different
security boundaries. Do not expose a loopback editor server to the network.
Reload the runtime when registration or a launcher changes; existing sessions
can retain old tool lists and credentials. Read one known target before saying
the connection works. Chat histories and approval state do not synchronize.
