import { AppMood } from "@/components/app-mood"
import { AppHabit } from "@/components/app-habit"
import { Separator } from "@/components/ui/separator"

export default function Home() {
  return (
    <div className="m-8">
      <div className="m-8">
        <h2 className="scroll-m-20 pb-2 text-3xl font-semibold tracking-tight first:mt-0">
          moods
        </h2>
        <div className="flex gap-4">  
          <AppMood/>
          <AppMood/>
        </div>
      </div>

      <Separator className="my-4" />

      <div className="m-8">
      <h2 className="scroll-m-20 pb-2 text-3xl font-semibold tracking-tight first:mt-0">
        habits
      </h2>
      <div className="flex gap-4">  
        <AppHabit/>
        <AppHabit/>
      </div>
    </div>
    </div>
  )
}