## what problem am I solving?
These are the key aspects of stress, to me, that accentuate a negative feedback loop:
1. **Loss of objectivity**: stress itself distorts your perception--maintaining awareness of your mood, in the aggregate, can be difficult.
2. **Lack of visibility**: stress can be exacerbated by a tendency to *ignore how you feel and push through*. Don't get me wrong, I think persistence is great, but there's plenty of evidence to show that maintaining elevated levels of stress in the medium to long term is detrimental to your health. 
3. **Diminished communication**: when you're stressed you tend to be more irritable and that makes it harder to reach out to people.
4. **Regression**: when you're stressed you may tend to withdraw socially, and stop habits that are ironically constructive for you because you are "too busy".

## how does this tool help?
The above problem set tells me that if you're often in high stress situations/periods what you really need is an antifragile system. Another way to put this is concept vs execution. I want to be able to set some guidelines/protocols ahead of time that execute without additional effort.

Example cases where the system would notify you and optionally those closest to you:
- If you have been sustaining an elevated level of stress
- If your stress is spiking/increasing
- If you start to show signs of regression in your habits
- If you are experience increasing negative emotionality

Another aspect is that I think you can design the app such that you are more likely to actually use it. Simple hacks like how when you open Duolingo it'll immediately put you into the next lesson (reducing user actions). Visual stimulus, rewards, milestones etc.

## definitions
Changed my mind, I think mood have natural poles (e.g. stress/relaxation, content/discontent). As well as 5 being too much gradation for unipolar data.

- -2 - very stressed
- -1 - somewhat stressed
- 0 - neutral
- 1 - somewhat relaxed
- 2 - very relaxed

### habits
The properties I want are:
- Forgiveness - option to mark a habit as uncompleted (reasons outside of control) e.g. Duolingo streak freezes
- Incentives

## guiding principles
1. Every notification has truly useful/actionable information.
2. Absolutely minimize the number of actions that the user needs to take.

## execution
So what do I want the execution of this idea to look like?
- Want the system to have minimal portability issues and system requirements
- But also don't want to ever have to update the app as data grows
- Actually want to complete the project so focus on what's most useful to me first, any other improvements/generalisations are a plus
    - Therefore, want backend logic to be easily modifiable by other people because I can't be bothered to fully generalize the notifier logic

At first, I just want this to be a little app that just runs locally (privacy). And for sharing it'll just generate and send images + text. No need to be a central platform.

Data: SQLite
Backend: Python FastAPI
Frontend: idk yet

### data structures
- mood
    - name: e.g. stress, contentment, etc.
    - score: -2 to 2
    - time: datetime
- habits
    - name: journaling, exercise etc.
    - completed: yes | no | unable
    - time: datetime
    - milestones
        - streak_target
        - reward

## actionability
1. immediate action required
    - quite serious: stress should be elevated or confluence with other factors
    - can be clearer cut
2. pulse
    - confluence