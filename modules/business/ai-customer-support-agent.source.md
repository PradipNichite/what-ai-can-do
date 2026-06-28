# AI Customer Support Agent Source

This is the source-of-truth concept pack for the customer support example.

Renderers should use this source but should not copy the same layout.

## Core Learner Question

How can AI answer a customer support question without guessing?

## Familiar Situation

A customer ordered something online. The order has not arrived. The customer asks support what happened.

Use Indian examples:

- Flipkart-style order.
- Local Instagram or WhatsApp store.
- Courier delivery.
- Small business using Excel, WhatsApp, and courier dashboard.

## Human Workflow

1. Customer asks where the order is.
2. Support asks for Order ID, Mobile Number, or Email.
3. Support opens the company System.
4. Support searches the Order.
5. Support checks payment, courier status, and expected delivery.
6. Support explains the status in simple language.
7. Support creates a Ticket if needed.
8. Support hands over or escalates tricky cases.

## Weak AI Moment

AI without access can only give a generic answer.

Example:

> Delivery usually takes 3-5 days.

This does not answer the customer's actual question.

## Capable AI Moment

AI connected to tools can:

- Ask for missing details.
- Check Order System.
- Check courier status.
- Explain the specific status.
- Create a Ticket.
- Hand over to a human.

## Human Judgment Moment

Humans should handle:

- Refunds.
- Damaged items.
- Angry customers.
- Fraud or suspicious activity.
- Policy exceptions.
- Sensitive decisions involving money or trust.

## Big Idea

An AI Customer Support Agent is not just a chatbot. It is AI connected to a workflow, tools, trusted data, and human handover.

## Renderer Map

- Markdown visual journey: `modules/business/ai-customer-support-agent.md`
- Mobile image story: `outputs/mobile-stories/ai-customer-support-agent.md`
- Marathi captioned mobile story: `outputs/mobile-stories/ai-customer-support-agent.mr.md`
- Marathi video/storyboard script: `outputs/video-scripts/ai-customer-support-agent.mr.md`

## Sources

- Microsoft Learn: Copilot Studio overview - https://learn.microsoft.com/en-us/microsoft-copilot-studio/fundamentals-what-is-copilot-studio
- Salesforce Agentforce - https://www.salesforce.com/in/agentforce/
- McKinsey: generative AI and customer operations - https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/the-economic-potential-of-generative-ai-the-next-productivity-frontier
