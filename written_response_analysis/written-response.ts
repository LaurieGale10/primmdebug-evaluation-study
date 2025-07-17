import { DebuggingStage } from "./debugging-stage.ts";

export class WrittenResponse {

    private exercise: string;
    private exerciseDescription: string;
    private debuggingStage: DebuggingStage;
    private response: string;
    private code: string | null;

    constructor(exercise: string, exerciseDescription: string, debuggingStage: string, response: string, code: string | null = null) {
        this.response = response;
        this.exerciseDescription = exerciseDescription;
        this.debuggingStage = DebuggingStage[debuggingStage as keyof typeof DebuggingStage];
        this.exercise = exercise;
        this.code = code;
    }

    getExercise(): string {
        return this.exercise;
    }

    getExerciseDescription(): string {
        return this.exerciseDescription;
    }

    getDebuggingStage(): DebuggingStage {
        return this.debuggingStage;
    }

    getResponse(): string {
        return this.response;
    }
}