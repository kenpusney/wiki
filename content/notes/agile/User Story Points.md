
Story points are an important part of [[User Stories|user story mapping]], and many agile teams use them when planning their work. But they aren't as simple as adding numbers to tasks or estimating how long a job will take.

Even if you've been using story points for a while, you'll find that different teams and organizations will use them differently.

## What are story points?

Story points are a useful unit of measurement in agile. You assign a number to each user story to estimate the total effort required to bring a feature or function to life.

Story points are a unit of measure for expressing an estimate of the overall effort that will be required to fully implement a [[Sprint Backlog|product backlog]] item or any other piece of work.

When we estimate with story points, we assign a point value to each item. The raw values we assign are unimportant: Some teams use a [modified fibonacci sequence](#the-fibonacci-sequence-for-estimation) (1, 2, 3, 5, 8, 13); others use a doubling sequence (1, 2, 4, 8, 16).

What matters are the *relative values*. A user story that is assigned two story points should be twice as much effort as a one-point story. It should also be two-thirds the effort of a story that is estimated as three story points.

Instead of assigning 1, 2 and 3, that team could instead have assigned 100, 200 and 300. Or 1 million, 2 million and 3 million. It is the ratios that matter, not the actual numbers.

One of the main reasons story points are so valuable is that they allow team members with different skill levels to communicate about and agree on an estimate. Instead of arguing about how long it might take each team member personally to do something, teams instead can quickly say that this user story is about twice or three times as much effort as that user story. With story points, it's all relative.

## What factors go into a story point estimate?

Story points represent the **effort** to develop a user story or product backlog item. Effort is a question of time: how long it will take to finish something. Many factors go into determining effort, including:

- **The amount of work to do** — If there is more to do, the estimate of effort should be larger. There may be economies of scale, so 100 fields might not get 100 times more points than 1 field — perhaps only 2 or 3 or 10 times as much.
- **Complexity** — Work that is complex will require more thinking, more trial-and-error experimentation, perhaps more back-and-forth with a customer, may take longer to validate and may need more time for mistake corrections.
- **Risk and uncertainty** — If the stakeholder is unclear about what will be needed, that uncertainty should be reflected in the estimate. If implementing a feature involves changing old, brittle code with no automated tests, that risk should be reflected in the estimate.

### Remember the Definition of Done

A story point estimate must include everything involved in getting a product backlog item all the way to done. If a team's [[Definition of Done]] includes creating automated tests to validate the story, the effort to create those tests should be included in the story point estimate.

## When to estimate story points

User stories can be estimated during [[User Story Mapping|user story mapping]], [[Backlog Refinement|backlog refinement]], or during [[Sprint Planning|sprint planning]].

Once a user story has been defined, mapped to the backbone, and prioritized, it's time to estimate the story points. It is a good idea to work with your team to do this, as each team member plays a different role in different stories, and knows the work involved in UX, design, development, testing, and launching. Collaborating on story point estimation will also help you spot dependencies early.

It is best to assign story points to each user story before you sequence them into releases or sprints. This allows you to assess the complexity, effort, and uncertainty of each user story in comparison to others on their backlog, and to make informed decisions about the work you decide to commit to each sprint or release.

## How to estimate story points for the first time

Because story points are relative, you need to give yourself some baseline estimates for the first time you do story point estimation. This will give you a frame of reference for all future stories.

Start by choosing stories of several different sizes:
- One very small story
- One medium sized story
- One big story

Then assign points to each of these baseline stories. Your smallest story might be 1. If your medium story requires 3 times more effort, then it should be 3. If your big story requires 10 times the effort, it should be 10.

The important thing is that you'll be able to use these baseline stories to estimate all your future stories by comparing the relative amount of effort involved.

Over time, you and your team will find estimating user stories becomes easier as your shared understanding of the work develops.

## The Fibonacci sequence for estimation

The traditional Fibonacci series is 1, 2, 3, 5, 8, 13, 21, 34, 55 and so on. Each number is the sum of the two preceding numbers.

Many teams use a modified Fibonacci series: 1, 2, 3, 5, 8, 13, **20**, **40** and **100**.

### Why Fibonacci works: Weber's Law

Numbers that are too close to one another are impossible to distinguish as estimates.

Imagine being handed two weights — one is one kilogram and the other is two kilograms. With one in each hand but not able to see which is which, you can probably distinguish them. The two kg weight will feel noticeably heavier.

Imagine instead being handed a 20kg weight and a 21kg weight. They are the same one kg difference, but you would have a much harder time identifying the heavier of the two.

This is due to **Weber's Law**: the difference we can identify between objects is given by a percentage. The difference from one to two kilograms is 100%. The difference between 20 and 21kg is only 5%.

The values in the Fibonacci scale work well because they roughly correspond to Weber's Law. After the two (which is 100% bigger than one), each number is about 60% larger than the preceding value.

### Why modify the larger numbers?

Ultimately, an estimate of 21 implied a precision teams couldn't support. Stakeholders would look at the 21 and be impressed that the team called it 21 rather than rounding it to 20 or even 25.

Using 20 rather than 21 works well. Once you've deviated from the Fibonacci sequence once, you can introduce 40 and 100 — representing 100% and 150% increases over the preceding numbers.

### Fibonacci vs doubling sequence

Some teams prefer a simple doubling of numbers: 1, 2, 4, 8, 16, 32. Each worked equally well in practice. The main difference is that doubling sequences tend to focus discussions on "Is this double the size?", while Fibonacci sequences lead to discussions more about the work involved — which tends to be healthier.

## Why you should never equate story points to hours

Equating story points to a set number of hours **obviates the primary reason to use story points** in the first place.

### Story points are abstract on purpose

By using story points, agile teams with developers who work at different speeds can agree on estimates. A senior developer might be able to knock out a certain product backlog item in 8 hours, and a more junior developer might take 16 hours to do the same work, but they can both agree that it's a 1-point story.

With that agreement in place, they can look at another story and agree that it will take twice as much effort, so it should be worth two points.

### The relationship is a distribution, not an equivalence

The relationship between story points and hours is a **distribution**, not a fixed mapping. One-point items take from x to y hours. Two-point backlog items take from about 2x to 2y hours.

Some of the most time-consuming one-point items may take longer than some of the shortest two-point items. But the tails of, say, the one- and thirteen-point distributions will rarely overlap.

### Converting to hours complicates thinking

When story points are tied to a certain number of hours, team members no longer think abstractly. They mentally estimate first using hours, then convert to points — and different team members will get different results because they work at different speeds.

If someone wants to start translating story points to hours, just stop calling the units points and use hours or days instead. Calling them points when they're really hours introduces needless complexity.

### Convert to dollars instead

When stakeholders ask what story points "mean," convert to cost rather than time:

1. Gather data on how much the team has been paid over a period of time
2. Divide total team compensation by the number of story points delivered → **cost per point**
3. Multiply the cost per point by the total expected size of the project

For example, if a team was paid $100,000 and delivered 100 story points, the cost per point is $1,000.

## Using story points to estimate [[Velocity|velocity]]

After some time working together, most teams will have a good idea about how much effort is involved in each story point. You should be able to estimate about as many story points as your team can manage during a two-week sprint.

For example, if your team can usually get through 3 story points per day, this might add up to 30 story points across a two-week sprint. This is your velocity.

Velocity is useful for [[User Story Mapping|user story mapping]] and [[Sprint Planning|sprint planning]]. When mapping your user stories to sprints or versions, you can check the total story points and make sure it matches up with your velocity so you're not over- or under-committed.

## Story points across agile methodologies

Story points are central to estimation and planning processes in many agile methodologies:

- **Scrum** teams use story points during sprint planning to decide which tasks to include, encouraging discussion that leads to shared context
- **Extreme Programming (XP)** uses story points to assess the size of features, enabling teams to prioritize and allocate resources effectively
- **Kanban** teams can benefit from story points by using them to set work-in-progress limits and optimize the flow of tasks

## Scrum, story points, and conversations

Conversations are an essential component of agile estimating. Even with thought exercises like story points as buckets, team members often don't agree at first on how much effort a story will be.

These varying estimates can spark illuminating conversations between team members and with product owners about acceptance criteria, approach, and other factors that can affect how much effort it will take to complete an item.

The power of these conversations is one of the reasons many teams use [[Agile Estimation#Planning Poker|planning poker]]. Planning poker is a fun way to estimate, and it's also a way to keep each person's estimate private until the team members all reveal their cards.

Once the team has agreed on an estimate, it assigns story points to the backlog item. That story point estimate is later used in calculating a team's average sprint velocity, capacity, and more.
