import { DebuggingStage } from "./debugging-stage.ts";

export class WrittenResponse {

    private exercise: string;
    private debuggingStage: DebuggingStage;
    private response: string;

    constructor(exercise: string, debuggingStage: string, response: string) {
        this.response = response;
        this.debuggingStage = DebuggingStage[debuggingStage as keyof typeof DebuggingStage];
        this.exercise = exercise;
    }

    getExercise(): string {
        return this.exercise;
    }

    getDebuggingStage(): DebuggingStage {
        return this.debuggingStage;
    }

    getResponse(): string {
        return this.response;
    }
}