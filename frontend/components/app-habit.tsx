"use client"

import {
    Card,
    CardContent,
    CardDescription,
    CardFooter,
    CardHeader,
    CardTitle,
  } from "@/components/ui/card"
import { Button } from "./ui/button"
import { ThumbsUp, ThumbsDown, Pause } from "lucide-react"
 
import {
  ToggleGroup,
  ToggleGroupItem,
} from "@/components/ui/toggle-group"
import { toast } from "sonner"

function handleSub() {
    toast.success("[habit] set to [input] for [date]")
    // toast.error("failed to update [habit]", {description:"err details"})
}

export function AppHabit() {
    return (
        <Card>
            <CardHeader>
                <CardTitle>did you [habit] today?</CardTitle>
                <CardDescription>last updated: [time]</CardDescription>
            </CardHeader>
            <CardContent>
                <ToggleGroup type="single" size="lg" variant="outline">
                    <ToggleGroupItem value="yes">
                        <ThumbsUp className="h-4 w-4" />
                    </ToggleGroupItem>
                    <ToggleGroupItem value="no">
                        <ThumbsDown className="h-4 w-4" />
                    </ToggleGroupItem>
                    <ToggleGroupItem value="unable">
                        <Pause className="h-4 w-4" />
                    </ToggleGroupItem>
                </ToggleGroup>
            </CardContent>
            <CardFooter>
                <Button onClick={handleSub}>submit</Button>
            </CardFooter>
        </Card>
    )
}