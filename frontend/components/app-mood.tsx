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
import { Slider } from "@/components/ui/slider"
import { useState } from "react"
import { toast } from "sonner"



export function AppMood() {
    const [value, setValue] = useState(2)

    const getMoodText = (val: number) => {
        switch(val) {
            case 0: return "very [negative]"
            case 1: return "[negative]"
            case 2: return "neutral"
            case 3: return "[positive]" 
            case 4: return "very [positive]"
            default: return "neutral"
        }
    }

    function handleSub() {
        toast.success(`[positive] updated to ${getMoodText(value)}`)
        // toast.error("failed to update [positive]", {description:"err details"})
    }

    return (
        <Card>
            <CardHeader>
                <CardTitle>how [positive] are you?</CardTitle>
                <CardDescription>last updated: [time]</CardDescription>
            </CardHeader>
            <CardContent>
                <Slider 
                    defaultValue={[2]}
                    max={4} 
                    step={1}
                    onValueChange={(vals) => setValue(vals[0])}
                />
                <p className="text-sm text-muted-foreground">you are: {getMoodText(value)}</p>
            </CardContent>
            <CardFooter>
                <Button onClick={handleSub}>submit</Button>
            </CardFooter>
        </Card>
    )
}