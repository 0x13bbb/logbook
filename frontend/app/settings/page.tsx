import { ModeToggle } from "@/components/mode-toggle";

export default function Settings() {
    return (
        <div className="m-8">
            <h2 className="scroll-m-20 pb-2 text-3xl font-semibold tracking-tight first:mt-0">
                settings
            </h2>
            <div className="flex items-center">
                <p className="mr-4">theme: </p>
                <ModeToggle/>
            </div>
            <div className="flex items-center">
                <p className="mr-4">TODO: settings for notifier</p>
            </div>
            
        </div>
    )
}