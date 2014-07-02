import java.util.*;
import java.lang.Thread;

public class Fly 
{
	private int xCoordinate; // x coordinate of fly
	private int yCoordinate; // y coordinate of fly
	private long startTime; // First recording of fly
	private long mostRecentTime; // Most recent recording of fly
	private static int flyCount; // Number of flies on this slide

	public Fly (int x, int y, long tInitial)
	{
		flyCount++;
		this.xCoordinate = x;
		this.yCoordinate = y;
		this.startTime = tInitial;
	}

	public int getX() {
		return this.xCoordinate;
	}

	public int getY() {
		return this.yCoordinate;
	}

	public int getFlyCount() {
		return flyCount;
	}

	public void lastRecorded(long tMostRecent) {
		this.mostRecentTime = tMostRecent;
	}

	public long calculateTimeLeft(long standByTime) {
		long timeRemaining;
		long now = 0;

		timeRemaining = this.mostRecentTime + standByTime - now;

		if (timeRemaining < 0) {
			System.err.print("Oops. Remaining time is already up. Please try again");
			return -1;
		} else {
			return timeRemaining;
		}
	}

	public static void main(String[] args) {

		double then = System.currentTimeMillis();

		try {
			Thread.sleep(4000);
		} catch (InterruptedException e) {
			
		}

		double now = System.currentTimeMillis();

		double timeElapsed = (now-then)/1000;

		System.out.println(timeElapsed);

	}
}