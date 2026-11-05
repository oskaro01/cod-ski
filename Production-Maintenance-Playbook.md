# Production Maintenance Playbook for JavaScript and Python Developers

## What changes when the website goes live

Local development asks, "Does this feature work?"

Production asks:

- Does it work for real users, on real devices, at the current traffic level?
- What happens when the database is slow or unavailable?
- Can the team detect the failure before customers report it?
- Can the change be rolled back without destroying data?
- Can another developer understand the system at 3:00 AM?
- Are secrets, personal data, payments, and admin actions protected?
- Can the service recover after a restart, deploy, provider outage, or traffic spike?

Production maintenance is the discipline of keeping a changing system reliable, secure, observable, recoverable, and understandable.

No guide can list every failure in every system. The map below covers the failure families that repeatedly appear in web applications, APIs, background workers, databases, cloud infrastructure, and external integrations.

## The five production questions

For every feature or service, answer these questions:

1. **Change:** How will this be released safely?
2. **Health:** How will we know it is working?
3. **Failure:** What happens when a dependency or component fails?
4. **Recovery:** How do we restore service and data?
5. **Learning:** How do we prevent or reduce the next occurrence?

If the answer is only "we will check the server," the system is not operationally ready.

## 1. Release and change-management failures

Production failures often come from a correct change applied at the wrong time, in the wrong order, or with the wrong configuration.

Common obstacles:

- A release works locally but fails in the production build environment.
- A dependency lockfile is missing or different from the deployed artifact.
- The code was tested, but the exact artifact tested is not the artifact deployed.
- A required environment variable is missing or has the wrong name.
- A production-only feature flag is configured incorrectly.
- A rollout changes too many things at once, making diagnosis difficult.
- A deploy is started without a rollback plan.
- A release succeeds technically but breaks a business flow.
- A cache, CDN, browser, or service worker continues serving old assets.
- A deployment is interrupted halfway through.
- Two deploys overlap and the later deploy hides the original failure.
- A manual server change creates configuration drift.
- A hotfix bypasses review and becomes permanent undocumented behavior.
- A rollback restores application code but leaves an incompatible database schema.
- A release changes API behavior that another service or client still depends on.

Production habits:

- Build once and promote the same artifact through environments.
- Record the commit SHA, build ID, configuration revision, and migration revision.
- Use staging that resembles production enough to expose meaningful failures.
- Define rollback triggers before deployment.
- Release risky behavior behind a feature flag with a kill switch.
- Use canary, rolling, or blue-green deployment where the system justifies it.
- Keep deployments small and observable.

Google's release-engineering guidance emphasizes reproducible automated builds and repeatable releases, while GitHub Actions environments can restrict branches, secrets, and approval gates for production deployments. [Google SRE release engineering](https://sre.google/sre-book/release-engineering/), [GitHub deployment environments](https://docs.github.com/en/actions/concepts/workflows-and-actions/deployment-environments)

## 2. Database and data-correctness failures

Code can be rolled back. Data is harder. A bad migration, duplicate payment, or corrupted record may remain after the application is fixed.

Common obstacles:

- A migration locks a large table during peak traffic.
- A migration is backward-incompatible with the previous application version.
- A column is removed before every running instance stops using it.
- A migration succeeds in staging but times out on production-sized data.
- A query becomes slow because an index is missing or no longer useful.
- An ORM hides an N+1 query or loads too many rows into memory.
- A connection pool is too large and exhausts the database.
- A connection pool is too small and creates request queues.
- Transactions are too broad and hold locks longer than expected.
- Deadlocks occur under concurrent writes.
- Two requests update the same record and overwrite each other.
- A retry repeats a non-idempotent write.
- A webhook creates a duplicate order or payment.
- Read replicas return stale data.
- A cache shows old inventory, permissions, or prices.
- A backup exists but has never been restored successfully.
- A restore is too slow for the business recovery target.
- Backups are in the same account or region as the primary data.
- Encryption keys are unavailable when backups are needed.
- Time zones create incorrect expiry dates, reports, or billing periods.
- Money is stored in floating point instead of integer minor units or decimal types.
- A delete removes data that must be retained for audit, legal, or customer support reasons.
- A background job processes a record after the user has already changed or deleted it.

Safer database practices:

- Use versioned, reviewed migrations.
- Prefer expand, migrate, contract for incompatible schema changes.
- Make critical writes idempotent with unique keys or idempotency keys.
- Use constraints for invariants such as unique values, non-null fields, and valid ranges.
- Test migrations against production-like volume.
- Monitor query latency, locks, connection usage, replication lag, and storage.
- Test backup restoration on a schedule.

The production-readiness checklist reviewed from GitHub highlights migration compatibility, duplicate-request handling, durable writes, replay or reconciliation, capacity limits, and restore testing as separate concerns. [Production readiness checklist](https://github.com/happysnaker/production-readiness-checklist)

## 3. Availability and reliability failures

Availability failures are not limited to a server being down. A service can be technically up while users cannot complete their work.

Common obstacles:

- The process crashes on an unhandled exception.
- The process is alive but stuck in a deadlock or event-loop block.
- A health check reports success while the database connection is broken.
- A liveness check restarts a slow but healthy process and creates a restart loop.
- A readiness check sends traffic before the application has loaded required state.
- A dependency timeout consumes every application worker.
- A queue grows faster than workers can process it.
- A worker silently stops consuming messages.
- A service depends on one region, one instance, one disk, or one provider.
- A DNS, TLS certificate, domain, load balancer, or firewall problem blocks all traffic.
- A provider outage affects payments, email, storage, maps, search, or authentication.
- A retry storm overloads a dependency that is already failing.
- A circuit breaker is missing or configured too aggressively.
- A graceful degradation path was never designed.
- A maintenance task runs during peak traffic.
- A scheduled job runs twice after a clock, deployment, or retry issue.

Use timeouts on every network boundary. Use bounded retries with exponential backoff and jitter. Make retryable operations idempotent. Apply circuit breakers, queue limits, concurrency limits, and fallback behavior where appropriate.

Retries can make an incident worse when many callers retry together. Microsoft’s transient-fault guidance specifically recommends bounded retries, retry budgets, exponential backoff, circuit breakers, and idempotent operations. [Transient fault handling guidance](https://github.com/microsoftdocs/architecture-center/blob/main/docs/best-practices/transient-faults.md)

## 4. Performance, capacity, and scaling failures

Performance is a production correctness issue when users time out, abandon checkout, or cannot complete a task.

Common obstacles:

- A page ships a large JavaScript bundle or unoptimized images.
- A slow database query is hidden by a fast local dataset.
- An endpoint performs repeated queries inside a loop.
- A cache has a low hit rate or invalidation bug.
- Cache stampedes happen when many requests regenerate the same value.
- A hot key or hot partition overloads one database node.
- Memory grows over time until the process is killed.
- CPU is saturated by image processing, encryption, serialization, or accidental loops.
- Too many open file descriptors or sockets exhaust the process.
- Worker concurrency is higher than the database or API can handle.
- Autoscaling reacts too slowly or scales on the wrong signal.
- Autoscaling increases cost without fixing the bottleneck.
- A traffic spike exposes a single-threaded or synchronous bottleneck.
- A cold start exceeds the request timeout.
- A rate limit blocks legitimate customers or fails to stop abuse.
- Load tests measure average latency and hide tail latency at p95 or p99.
- A new feature increases response size and network transfer cost.
- Logs, metrics, and traces consume enough resources to affect the service.

Measure request rate, error rate, latency distribution, saturation, queue depth, database latency, cache hit rate, and resource usage. Capacity planning should include normal traffic, expected growth, sudden spikes, and dependency degradation.

## 5. Observability and debugging failures

Without observability, production maintenance becomes guesswork. A console log saying "something failed" is rarely enough.

Common obstacles:

- There are no logs for a critical business operation.
- Logs contain sensitive data or cannot be searched reliably.
- Logs use inconsistent levels and messages.
- Errors are swallowed or replaced with generic errors before being logged.
- Logs have no request ID, trace ID, user-safe correlation ID, or deployment version.
- Server and client clocks use different time zones.
- Metrics measure infrastructure but not user outcomes.
- Alerts fire on symptoms without identifying customer impact.
- Alert thresholds are noisy, stale, or never tested.
- The team has dashboards but no runbook for interpreting them.
- Traces are not propagated across services, queues, or external calls.
- High-cardinality labels create an expensive metrics system.
- Sampling removes the one trace needed to debug a rare failure.
- Monitoring sees the backend but not the browser, checkout, email, or payment flow.
- The service is failing silently because health checks only test process existence.
- No one knows which deployment changed the error rate.

Instrument three signal families:

- **Metrics:** rates, counts, distributions, saturation, business outcomes.
- **Logs:** structured events with useful context and redacted sensitive data.
- **Traces:** the path of a request across services, queues, databases, and providers.

OpenTelemetry describes observability as the ability to ask why a system behaves a certain way using correlated traces, metrics, and logs. [OpenTelemetry observability primer](https://opentelemetry.io/docs/concepts/observability-primer/)

## 6. Security and privacy failures

Production security is broader than avoiding SQL injection. It includes access, secrets, dependencies, infrastructure, logs, backups, and operations.

Common obstacles:

- Secrets are committed to Git, printed in logs, or included in error reports.
- A leaked token is deleted from the repository but not rotated.
- Production credentials have more permissions than the service needs.
- Development and production share credentials.
- Authentication is implemented but authorization is missing.
- An object ID lets one user access another user’s data.
- Admin routes are hidden in the UI but not protected on the server.
- Session cookies lack secure, HTTP-only, or same-site controls.
- Password reset tokens are predictable, reusable, or never expire.
- Refresh tokens are not revoked after account compromise.
- CORS allows unintended origins or credentials.
- CSRF protection is missing for cookie-authenticated state changes.
- XSS enters through user content, unsafe HTML, or template interpolation.
- SQL, NoSQL, command, path, or template injection reaches an interpreter.
- SSRF lets users make the server request internal services.
- File uploads allow malware, oversized files, path traversal, or unsafe content types.
- Rate limits do not protect login, password reset, search, or expensive endpoints.
- Error pages reveal stack traces, framework versions, SQL, or filesystem paths.
- Dependency or container vulnerabilities are not patched.
- A CI workflow runs untrusted pull-request content with production secrets.
- Third-party packages or GitHub Actions are not pinned or reviewed.
- TLS, security headers, debug endpoints, directory listings, or default accounts are misconfigured.
- Logs and backups contain personal data without retention, access, or deletion rules.
- A security incident has no evidence-preservation or notification process.

Use threat modeling for important flows, least-privilege credentials, dependency scanning, secret scanning, secure headers, input validation, authorization tests, patching, and a tested incident response path. OWASP’s security-program guidance includes patching, monitoring, scanning, reporting, incident response, supply-chain protection, and disaster recovery as operational responsibilities. [OWASP security program guidance](https://github.com/OWASP/Top10/blob/master/2025/docs/en/0x03_2025-Establishing_a_Modern_Application_Security_Program.md)

## 7. Frontend and browser failures

Frontend production failures often appear only on a particular browser, device, network, locale, or cached version.

Common obstacles:

- Hydration mismatch or client-only code breaks the initial page.
- A browser-specific API is unsupported.
- JavaScript fails and the page has no useful fallback.
- A stale service worker serves incompatible assets.
- CDN caching serves an old HTML file with new JavaScript, or the reverse.
- CSS breaks at an untested viewport or text length.
- Forms lose user input after an error.
- Optimistic UI shows success before the server confirms the action.
- Race conditions show stale search results or the wrong user state.
- Accessibility regressions block keyboard, screen-reader, or low-vision users.
- Focus management fails in modals and validation errors.
- A third-party script blocks rendering or leaks data.
- Consent, analytics, or tracking behavior changes after a tag update.
- Localization breaks dates, currencies, RTL text, or pluralization.
- Time-zone behavior differs between browser and server.
- SEO metadata, canonical URLs, robots rules, sitemap, or structured data break.
- Error and loading states were never designed for slow networks.

Test the critical user journeys on representative browsers and devices. Add browser monitoring, performance budgets, accessibility checks, and error-path tests to CI where practical.

## 8. API and external-integration failures

Every external service is a dependency with its own uptime, limits, schema, pricing, and failure behavior.

Common obstacles:

- The provider changes a response field or removes an endpoint.
- API version or SDK support expires.
- Rate limits or quotas are reached.
- Authentication tokens expire during a request.
- Webhooks arrive late, out of order, duplicated, or not at all.
- Signature verification uses the wrong raw request body.
- A payment succeeds at the provider but the callback fails locally.
- A shipment, email, SMS, or refund is created twice after a retry.
- Provider timeouts leave local state uncertain.
- A provider returns a successful response with incomplete data.
- Sandbox behavior differs from production.
- Provider data has a different currency, time zone, encoding, or rounding rule.
- An integration has no reconciliation job for missed events.
- Vendor pricing or terms change unexpectedly.
- The only person who knows the integration leaves the team.

For every integration document authentication, timeout, retry, idempotency, webhook verification, event replay, reconciliation, rate limits, provider status page, support contact, and fallback behavior.

## 9. Background jobs and asynchronous systems

Queues make systems more resilient, but they introduce time, ordering, duplication, and visibility problems.

Common obstacles:

- A job is accepted but never processed.
- A worker crashes after performing the side effect but before acknowledging the message.
- A job is delivered twice.
- A retry queue grows forever.
- Poison messages repeatedly fail and block useful work.
- Job ordering is assumed but not guaranteed.
- A job uses stale user or product data.
- A scheduled job runs in two instances at the same time.
- Worker memory leaks slowly.
- Backpressure is hidden until the queue is hours behind.
- A deployment changes the job format while old workers are still running.
- No dead-letter queue or replay procedure exists.

Design jobs to be idempotent, observable, bounded, retryable only when safe, and replayable when business-critical. Monitor queue depth, age of oldest message, success rate, retry count, dead-letter count, and processing latency.

## 10. Infrastructure and cloud failures

Common obstacles:

- DNS records point to the wrong service or expire during migration.
- TLS certificates expire or are issued for the wrong hostname.
- Firewall, security group, WAF, or network policy blocks required traffic.
- Cloud quotas prevent scaling or deployment.
- IAM permissions work in one account but not another.
- A region, availability zone, storage bucket, or managed service becomes unavailable.
- Terraform or infrastructure code drifts from the actual environment.
- An emergency manual fix is never recorded in code.
- Storage fills because logs, uploads, or temporary files are not retained or deleted.
- A resource is public when it should be private.
- Cost increases from a leak, retry storm, oversized logs, or autoscaling loop.
- The provider has a shared-responsibility boundary the team misunderstands.
- A container image contains a vulnerable package or runs as root.
- A deployment tool or CI runner becomes the bottleneck during an incident.

Keep infrastructure changes reviewable and reproducible. Document ownership, quotas, dependencies, regions, recovery steps, and cost signals.

## 11. Domains, email, and business operations

These failures are easy to overlook because they live outside application code.

- Domain renewal fails.
- DNS propagation is misunderstood during a change.
- Email authentication is missing or broken: SPF, DKIM, or DMARC.
- Transactional email goes to spam or stops because a provider quota is reached.
- Contact, signup, checkout, or password-reset forms silently fail.
- Web analytics stops collecting data after a frontend change.
- Legal pages, privacy settings, or cookie consent are missing or stale.
- Prices, tax, currency, inventory, shipping, and refund rules disagree across systems.
- Support cannot see the request ID or order state needed to help the customer.
- A third-party service is paid from a personal account and expires.

Test the whole customer journey, including the email inbox, payment result, order state, support workflow, and refund path.

## 12. Human and organizational failures

Senior engineers reduce operational uncertainty for the team, not only for themselves.

- No clear service owner exists.
- The on-call person does not have access to dashboards or deployment tools.
- A runbook is outdated or assumes knowledge that is not written down.
- Alerts have no severity or escalation policy.
- Incidents are discussed in multiple channels with conflicting timelines.
- People make changes during an incident without recording them.
- Customer communication is delayed or too technical.
- A postmortem blames a person instead of improving the system.
- Action items have no owner or due date.
- The team repeats the same incident because fixes are not tracked.
- Engineers fear alerts, so alert quality declines.
- Operations knowledge exists only in one developer's memory.

Use a clear incident commander, a separate technical investigation lead, a communications owner when needed, a shared timeline, and a short list of owned follow-up actions. A good postmortem records impact, timeline, contributing factors, what went well, what went wrong, what could have been worse, and specific owned actions. [PagerDuty postmortem process](https://github.com/PagerDuty/incident-response-docs/blob/master/docs/after/post_mortem_process.md)

## What to do during an incident

1. Confirm the symptom and customer impact.
2. Declare the incident at the appropriate severity.
3. Assign an incident commander and record the timeline.
4. Stop risky changes and preserve evidence.
5. Check recent deploys, configuration changes, dependency health, traffic, errors, latency, saturation, and queue depth.
6. Choose the safest mitigation: rollback, disable a feature, shed load, fail over, pause a job, or degrade gracefully.
7. Verify recovery using user-facing signals, not only process health.
8. Communicate status in language customers and support can use.
9. Keep monitoring after the first recovery signal.
10. Write a blameless postmortem and create a small number of specific action items.

Do not change five unrelated things at once. It destroys the evidence needed to understand the incident.

## A production readiness review

Before releasing a meaningful feature, ask:

### Ownership and access

- Is there a named owner?
- Is there an on-call or escalation route?
- Can the owner deploy, inspect logs, see metrics, and roll back?

### Change safety

- Are CI checks green?
- Was the release built from a known commit?
- Is the deployment strategy defined?
- Are feature flags and rollback triggers ready?
- Are database migrations compatible with old and new code?

### Health and observability

- Are user-facing success, error, latency, and business metrics visible?
- Are logs structured and redacted?
- Can a request be traced across services and jobs?
- Does every important alert have a runbook?

### Data and recovery

- Are backups recent, protected, and restorable?
- Has restore been tested?
- Are destructive operations reversible or carefully staged?
- Is the recovery time and recovery point expectation understood?

### Security

- Are secrets outside source control?
- Are authentication and authorization tested separately?
- Are dependencies, images, and workflows scanned?
- Are admin routes, uploads, webhooks, and rate limits protected?

### User experience

- Does the main journey work on slow networks and representative devices?
- Are loading, empty, error, and retry states clear?
- Are accessibility, SEO, localization, and privacy behavior checked?

Google describes a production-readiness review as covering architecture, dependencies, monitoring, emergency response, capacity, change management, performance, and availability. [Google SRE production-readiness review](https://sre.google/sre-book/evolving-sre-engagement-model/)

## Maintenance cadence

### Every deploy

- Confirm commit, artifact, migrations, flags, owner, and rollback.
- Watch error rate, latency, saturation, business outcomes, and logs.
- Verify the critical user journey.

### Weekly

- Review incidents, near misses, noisy alerts, failed jobs, and open action items.
- Review dependency updates and security findings.
- Check storage, database growth, queue age, and cloud costs.
- Test one runbook step or recovery path.

### Monthly

- Restore a backup in a safe environment.
- Review certificates, domains, access permissions, secrets rotation, and provider quotas.
- Run a performance and accessibility check.
- Review slow queries and unused infrastructure.
- Check that documentation matches the deployed system.

### Quarterly

- Run a failure exercise or game day.
- Review disaster recovery and business continuity.
- Reassess architecture, capacity, cost, and dependency risk.
- Remove unused accounts, features, packages, and infrastructure.
- Review postmortem trends and repeated failure causes.

## Practical JavaScript and Python stack

You do not need every platform. Build one complete system and learn the operational ideas through it.

### Application

- JavaScript: Node.js with Fastify, Express, NestJS, or Next.js.
- Python: FastAPI, Django, or Flask.
- PostgreSQL for durable relational data.
- Redis for carefully scoped caching, rate limits, or queues.

### Delivery

- GitHub Actions for linting, tests, builds, security checks, and deployment.
- Docker for repeatable local and deployment environments.
- A managed platform first; Kubernetes later when you understand why you need it.

### Observability

- Sentry or an equivalent error tracker.
- OpenTelemetry for traces and correlated telemetry.
- A metrics and dashboard system such as Prometheus and Grafana when the service needs it.

### Operations

- Health and readiness endpoints.
- Structured logs with request IDs.
- Database migration tool native to your framework.
- Queue worker and dead-letter handling for long tasks.
- A written runbook and a rollback command.

## Your junior-to-mid-to-senior progression

### Stage 1: Operate one service

Deploy a real JavaScript or Python application with a database. Configure environment variables, HTTPS, logs, health checks, backups, and a domain. Fix a real production-like failure instead of only adding features.

### Stage 2: Make releases safe

Add CI, protected main branch, automated tests, migrations, staging, deployment history, feature flags, rollback, and smoke tests. Practice deploying a bad version and recovering from it.

### Stage 3: Make failures diagnosable

Add structured logs, request IDs, error tracking, metrics, traces, alerts, dashboards, and runbooks. Simulate a slow database, failed provider, stuck worker, expired token, and high error rate.

### Stage 4: Make data and integrations reliable

Implement idempotency, webhook verification, retries with backoff, circuit breaking, queue visibility, reconciliation, backup restoration, and safe schema evolution.

### Stage 5: Think in service boundaries

Learn capacity planning, SLOs, error budgets, threat modeling, cost controls, disaster recovery, dependency contracts, and progressive delivery. Review another developer's production-readiness plan and explain the tradeoffs.

### Stage 6: Lead the system, not just the code

Define operational standards, improve incident response, reduce recurring toil, mentor others, make risk visible, and choose the simplest architecture that meets the product's actual needs.

## Projects that will build real production skill

1. Deploy a full-stack app with a database and a real domain.
2. Add CI that runs tests, linting, type checks, dependency checks, and a production build.
3. Create a staged deployment with a documented rollback.
4. Add a database migration using expand, migrate, contract.
5. Build a webhook receiver with signature verification, idempotency, retries, and replay.
6. Add a queue worker with dead-letter handling and queue-age alerts.
7. Add logs, metrics, traces, error tracking, and a dashboard for one user journey.
8. Run a load test and fix the first real bottleneck.
9. Back up the database, destroy a test environment, and restore it.
10. Run a game day: simulate a bad deploy, database timeout, provider outage, expired secret, and queue backlog.
11. Write a blameless postmortem for one simulated incident.
12. Review the app against the production-readiness checklist every month.

## The standard to aim for

A mid-level developer can operate the features they build, diagnose common failures, make safe changes, and explain tradeoffs.

A senior developer builds systems and team practices that make those things easier for everyone else. They think about failure before it happens, make recovery a designed feature, and leave behind evidence, automation, and clear decisions.

## References and GitHub playbooks

- [Google SRE release engineering](https://sre.google/sre-book/release-engineering/)
- [Google SRE production-readiness review](https://sre.google/sre-book/evolving-sre-engagement-model/)
- [Google SRE monitoring distributed systems](https://sre.google/sre-book/monitoring-distributed-systems/)
- [OpenTelemetry observability primer](https://opentelemetry.io/docs/concepts/observability-primer/)
- [The Twelve-Factor App: config](https://12factor.net/config)
- [The Twelve-Factor App: logs](https://12factor.net/logs)
- [GitHub deployment environments](https://docs.github.com/en/actions/concepts/workflows-and-actions/deployment-environments)
- [GitHub Actions secure use](https://docs.github.com/en/actions/reference/security/secure-use)
- [Kubernetes probes](https://kubernetes.io/docs/concepts/workloads/pods/probes/)
- [OWASP application security program guidance](https://github.com/OWASP/Top10/blob/master/2025/docs/en/0x03_2025-Establishing_a_Modern_Application_Security_Program.md)
- [GitHub production-readiness checklist](https://github.com/happysnaker/production-readiness-checklist)
- [GitHub website-care checklist](https://github.com/TicketWaveHQ/website-care-checklist)
- [GitHub incident postmortem playbook](https://github.com/sigmadigitalza/engineering-playbook/blob/main/docs/playbooks/incident-postmortem.md)
